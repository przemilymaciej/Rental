from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BookGenre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre"
    )
    def __str__(self):
        return self.name



class Book(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    genre = models.ForeignKey('BookGenre', on_delete=models.PROTECT, null=True)
    ISBN = models.CharField(max_length=13, unique=True)


    class Meta:
        unique_together = ('author','title','genre',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FilmGenre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre"
    )
    def __str__(self):
        return self.name

class Film(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    genre = models.ForeignKey('FilmGenre', on_delete=models.PROTECT, null=True)
    length = models.DecimalField(max_digits=3, decimal_places=2)
    borrowed = models.BooleanField(
        default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('director','title','length',)


class CD(models.Model):
    whoAdd = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    band = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    tracks = models.TextField()
    length = models.DecimalField(max_digits=3, decimal_places=2)
    borrowed = models.BooleanField(
        default=False)
    class Meta:
        unique_together = ('genre','tracks',)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
