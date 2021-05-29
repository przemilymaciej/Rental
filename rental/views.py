from .models import Book
from .models import Film
from .models import BookRentHistory
from .models import FilmRentHistory
from .models import CD
from .models import CDRentHistory
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookForm, FilmForm, CDForm
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


class RankingView(generic.TemplateView):
    template_name='rental/stats.html'

    def get_context_data(self, **kwargs):
        context = super(RankingView, self).get_context_data(**kwargs)
        context.update({
            'top_5_CD': User.objects.annotate(num_CDs=Count('CDs')).order_by('-num_CDs')[:5],
            'top_5_films': User.objects.annotate(num_films=Count('films')).order_by('-num_films')[:5],
            'top_5_books': User.objects.annotate(num_books=Count('CDs')).order_by('-num_books')[:5],
        })
        return context


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
def confirm_rent_viewb(request, slug):
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


class FilmListView(generic.ListView):
    template_name = 'rental/films.html'
    model = Film

    def get_context_data(self, **kwargs):
        context = super(FilmListView, self).get_context_data(**kwargs)
        context.update({
            'top_3_films': Film.objects.order_by('-popularity')[:3],
        })
        return context

    def get_queryset(self):
        return Film.objects.order_by('-id')[:3]


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'rental/film_detail.html'
    def get_success_url(self):
        return reverse('books:filmDetail', kwargs={'slug': self.object.slug})



@login_required(login_url='users/login')
def f_confirm_rent_view(request, slug):
    try:
        f = Film.objects.get(slug=slug)
        if f.film_amount <= 0:
            messages.warning(
                request, f'You cant rent this film')
            return redirect('books:filmDetail', slug=f.slug)
    except Film.DoesNotExist:
        raise Http404("We dont have this film")
    return render(request, 'rental/f_confirm_rent_view.html', {'film': f})


@login_required(login_url='users/login')
def rent_film_view(request, slug):
    try:
        f = Film.objects.get(slug=slug)
        if f:
            if f.film_amount > 0:
                f.film_amount -= 1
                f.popularity += 1
                f.genre.popularity += 1
                f.save()
                log_history = FilmRentHistory(user=request.user, film=f)
                log_history.save()
                messages.success(
                    request, f'You rent a film: {f.title}')
            else:
                messages.warning(
                    request, f'You cant rent this film')
                return redirect('books:filmDetail', slug=f.slug)
    except Film.DoesNotExist:
        raise Http404("Film is unavailable")
    return redirect('books:films')


@login_required(login_url='users/login')
def return_film_view(request, slug):
    try:
        f = Film.objects.filter(slug=slug)[0]
        if f:
            f.film_amount += 1
            f.save()
            log_history = FilmRentHistory.objects.filter(film=f)[0]
            log_history.back_date = datetime.now()
            log_history.save()
            messages.success(
                request, f'You successfully returned a film: {f.title}')
        else:
            messages.warning(
                request, f'Error occurs, sorry')
            return redirect('UserProfile')
    except Film.DoesNotExist:
        raise Http404("Film is unavailable now ")
    return redirect('books:films')

class FilmUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Film
    form_class = FilmForm
    success_url = reverse_lazy('books:films')

class FilmCreateView(LoginRequiredMixin, generic.CreateView):
    model = Film
    form_class = FilmForm
    success_url = reverse_lazy('books:films')

class FilmDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Film
    success_url = reverse_lazy('books:films')

class SearchFilmListView(generic.ListView):
    template_name = "rental/film_search_result.html"
    model = Film

    def get_queryset(self):
        queryset = super(SearchFilmListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            film_by_genre = queryset.filter(genre__name__icontains=q).order_by('-popularity')
            return film_by_genre
        return queryset


class CDListView(generic.ListView):
    template_name = 'rental/CDs.html'
    model = CD

    def get_context_data(self, **kwargs):
        context = super(CDListView, self).get_context_data(**kwargs)
        context.update({
            'top_3_CDs': CD.objects.order_by('-popularity')[:3],
        })
        return context

    def get_queryset(self):
        return CD.objects.order_by('-id')[:3]


class CDDetailView(generic.DetailView):
    model = CD
    template_name = 'rental/cd_detail.html'
    def get_success_url(self):
        return reverse('books:cdDetail', kwargs={'slug': self.object.slug})


@login_required(login_url='users/login')
def cd_confirm_rent_view(request, slug):
    try:
        cd = CD.objects.get(slug=slug)
        if cd.CD_amount <= 0:
            messages.warning(
                request, f'You cant rent this CD')
            return redirect('books:cdDetail', slug=cd.slug)
    except Film.DoesNotExist:
        raise Http404("We dont have this CD")
    return render(request, 'rental/cd_confirm_rent_view.html', {'cd': cd})


@login_required(login_url='users/login')
def rent_cd_view(request, slug):
    try:
        cd = CD.objects.get(slug=slug)
        if cd:
            if cd.CD_amount > 0:
                cd.CD_amount -= 1
                cd.popularity += 1
                cd.genre.popularity += 1
                cd.save()
                log_history = CDRentHistory(user=request.user, cd=cd)
                log_history.save()
                messages.success(
                    request, f'You rent a CD: {cd.title}')
            else:
                messages.warning(
                    request, f'You cant rent this CD')
                return redirect('books:cdDetail', slug=cd.slug)
    except Film.DoesNotExist:
        raise Http404("CD is unavailable")
    return redirect('books:CDs')


@login_required(login_url='users/login')
def return_cd_view(request, slug):
    try:
        cd = CD.objects.filter(slug=slug)[0]
        if cd:
            cd.CD_amount += 1
            cd.save()
            log_history = CDRentHistory.objects.filter(cd=cd)[0]
            log_history.back_date = datetime.now()
            log_history.save()
            messages.success(
                request, f'You successfully returned a CD: {cd.title}')
        else:
            messages.warning(
                request, f'Error occurs, sorry')
            return redirect('UserProfile')
    except Film.DoesNotExist:
        raise Http404("Film is unavailable now ")
    return redirect('books:CDs')


class CDUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CD
    form_class = CDForm
    success_url = reverse_lazy('books:CDs')

class CDCreateView(LoginRequiredMixin, generic.CreateView):
    model = CD
    form_class = CDForm
    success_url = reverse_lazy('books:CDs')

class CDDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CD
    success_url = reverse_lazy('books:CDs')


class SearchCDListView(generic.ListView):
    template_name = "rental/cd_search_result.html"
    model = CD

    def get_queryset(self):
        queryset = super(SearchCDListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            cd_by_genre = queryset.filter(genre__name__icontains=q).order_by('-popularity')
            return cd_by_genre
        return queryset