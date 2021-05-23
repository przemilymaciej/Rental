from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('borrower','title', 'author', 'genre','ISBN')
