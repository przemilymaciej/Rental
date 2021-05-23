from .models import Book
from .models import Film
from .models import CD
from django.views import generic
from django.urls import reverse_lazy
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(generic.TemplateView):
    template_name='rental/main_page.html'


class BookListView(generic.ListView):
    model = Book

class AvailibleBookListView(generic.ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(borrower__isnull=True)
    template_name='rental/available.html'

class MyBooksListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'my-borrowed'
    template_name='rental/mybooks.html'

    def get_queryset(self):
        return Book.objects.filter(borrower=self.request.user)

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('rental:book_list')

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('rental:book_list')

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy('rental:book_list')


