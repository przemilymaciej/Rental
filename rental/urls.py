from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .models import Book
app_name = 'books'

urlpatterns = [
    path('', view=views.HomePageView.as_view(), name='home_page'),
    path('books', view=views.BookListView.as_view(), name='books'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='bookDetail'),
    path('confirm-rent-a-book/<slug:slug>', views.confirm_rent_view, name="confirm_rent_view"),
    path('book/rent-book/<slug:slug>', views.rent_book_view, name='rent_book'),
    path('book/return-book/<slug:slug>', views.return_book_view, name='return_book'),
    path('edit/<int:pk>', view=views.BookUpdateView.as_view(), name='book_edit'),
    path('new', view=views.BookCreateView.as_view(), name='book_new'),
    path('delete/<int:pk>', view=views.BookDeleteView.as_view(), name='book_delete'),
    path('search-book-results/', view=views.SearchBookListView.as_view(), name='search')
]