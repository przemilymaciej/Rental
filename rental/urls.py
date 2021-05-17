from django.urls import path
from . import views

urlpatterns = [
    path('books', views.book_list, name='book_list'),
    path('films', views.film_list, name='film_list'),
    path('CDs', views.CD_list, name='CD_list'),
    path('', views.main_page, name='main_page')
]