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
    path('confirm-rent-a-book/<slug:slug>', views.confirm_rent_viewb, name="confirm_rent_viewb"),
    path('book/rent-book/<slug:slug>', views.rent_book_view, name='rent_book'),
    path('book/return-book/<slug:slug>', views.return_book_view, name='return_book'),
    path('editb/<int:pk>', view=views.BookUpdateView.as_view(), name='book_edit'),
    path('newb', view=views.BookCreateView.as_view(), name='book_new'),
    path('deleteb/<int:pk>', view=views.BookDeleteView.as_view(), name='book_delete'),
    path('search-book-results/', view=views.SearchBookListView.as_view(), name='searchb'),
    path('films', view=views.FilmListView.as_view(), name='films'),
    path('film/<slug:slug>', views.FilmDetailView.as_view(), name='filmDetail'),
    path('confirm-rent-a-film/<slug:slug>', views.f_confirm_rent_view, name="f_confirm_rent_view"),
    path('film/rent-film/<slug:slug>', views.rent_film_view, name='rent_film'),
    path('film/return-film/<slug:slug>', views.return_film_view, name='return_film'),
    path('editf/<int:pk>', view=views.FilmUpdateView.as_view(), name='film_edit'),
    path('newf', view=views.FilmCreateView.as_view(), name='film_new'),
    path('deletef/<int:pk>', view=views.FilmDeleteView.as_view(), name='film_delete'),
    path('search-film-results/', view=views.SearchFilmListView.as_view(), name='searchf'),
    path('CDs', view=views.CDListView.as_view(), name='CDs'),
    path('cd/<slug:slug>', views.CDDetailView.as_view(), name='cdDetail'),
    path('confirm-rent-a-cd/<slug:slug>', views.cd_confirm_rent_view, name="cd_confirm_rent_view"),
    path('cd/rent-cd/<slug:slug>', views.rent_cd_view, name='rent_cd'),
    path('cd/return-cd/<slug:slug>', views.return_cd_view, name='return_cd'),
    path('editcd/<int:pk>', view=views.CDUpdateView.as_view(), name='cd_edit'),
    path('newcd', view=views.CDCreateView.as_view(), name='cd_new'),
    path('deletecd/<int:pk>', view=views.CDDeleteView.as_view(), name='cd_delete'),
    path('search-cd-results/', view=views.SearchCDListView.as_view(), name='searchcd'),
    path('stats/', view=views.RankingView.as_view(), name='ranking')

]