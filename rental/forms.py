from django import forms

from .models import Book

from .models import Film

from .models import CD


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre','ISBN','book_amount')

class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ('title', 'director', 'genre','length','film_amount')

class CDForm(forms.ModelForm):

    class Meta:
        model = CD
        fields = ('title', 'band', 'genre','length','CD_amount','tracks')


