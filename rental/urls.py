from django.urls import path
from . import views
from .models import Book
app_name = 'books'

urlpatterns = [
    path('', view=views.HomePageView.as_view(), name='home_page'),
    path('allbooks', view=views.BookListView.as_view(), name='book_list'),
    path('books', view=views.AvailibleBookListView.as_view(), name='available_books'),
    path('mybooks', view=views.MyBooksListView.as_view(), name='my_borrowed_books'),
    path('edit/<int:pk>', view=views.BookUpdateView.as_view(), name='book_edit'),
    path('new', view=views.BookCreateView.as_view(), name='book_new'),
    path('delete/<int:pk>', view=views.BookDeleteView.as_view(), name='book_delete'),
]