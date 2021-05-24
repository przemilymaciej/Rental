from .models import Book
from .models import Film
from .models import CD
from .models import BookRentHistory
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic.edit import FormMixin
from django.contrib import messages
from datetime import datetime


class HomePageView(generic.TemplateView):
    template_name='rental/main_page.html'


class BookListView(generic.ListView):
    template_name = 'rental/books.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context.update({
            'top_3_books': Book.objects.order_by('-popularity')[:3],
        })
        return context

    def get_queryset(self):
        return Book.objects.order_by('-id')[:3]


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'rental/book_detail.html'
    def get_success_url(self):
        return reverse('books:bookDetail', kwargs={'slug': self.object.slug})


class SearchBookListView(generic.ListView):
    template_name = "books/book_search_result.html"
    model = Book

    def get_queryset(self):
        queryset = super(SearchBookListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            books_by_genre = queryset.filter(genre__name__icontains=q).order_by('-popularity')
            return books_by_genre
        return queryset

@login_required(login_url='users/login')
def confirm_rent_view(request, slug):
    try:
        b = Book.objects.get(slug=slug)
        if b.book_amount <= 0:
            messages.warning(
                request, f'You cant rent this book')
            return redirect('books:bookDetail', slug=b.slug)
    except Book.DoesNotExist:
        raise Http404("We dont have this book")
    return render(request, 'rental/confirm_rent_view.html', {'book': b})


@login_required(login_url='users/login')
def rent_book_view(request, slug):
    try:
        b = Book.objects.get(slug=slug)
        if b:
            if b.book_amount > 0:
                b.book_amount -= 1
                b.popularity += 1
                b.genre.popularity += 1
                b.save()
                log_history = BookRentHistory(user=request.user, book=b)
                log_history.save()
                messages.success(
                    request, f'You rent a book: {b.title}')
            else:
                messages.warning(
                    request, f'You cant rent this book')
                return redirect('books:bookDetail', slug=b.slug)
    except Book.DoesNotExist:
        raise Http404("Book is unavailable")
    return redirect('books:books')


@login_required(login_url='users/login')
def return_book_view(request, slug):
    try:
        b = Book.objects.filter(slug=slug)[0]
        if b:
            b.book_amount += 1
            b.save()
            log_history = BookRentHistory.objects.filter(book=b)[0]
            log_history.back_date = datetime.now()
            log_history.save()
            messages.success(
                request, f'You successfully returned a book: {b.title}')
        else:
            messages.warning(
                request, f'Error occurs, sorry')
            return redirect('UserProfile')
    except Book.DoesNotExist:
        raise Http404("Book is unavailable now ")
    return redirect('books:books')


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')


