from django.shortcuts import render
from .models import Book
from .models import Film
from .models import CD

def book_list(request):
    books = Book.objects.filter(borrowed=False)
    return render(request, 'rental/book_list.html', {'books':books})


def film_list(request):
    films = Film.objects.filter(borrowed=False)
    return render(request, 'rental/film_list.html', {'films':films})

def CD_list(request):
    CDs = CD.objects.filter(borrowed=False)
    return render(request, 'rental/CD_list.html', {'CDs':CDs})

def main_page(request):
    return render(request, 'rental/main_page.html', {})
