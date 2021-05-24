from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BookGenre(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a book genre"
    )
    slug = models.SlugField(unique=True)

    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BookGenre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "BookGenres"


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=50)
    genre = models.ForeignKey('BookGenre', on_delete=models.PROTECT, null=True)
    ISBN = models.CharField(max_length=13, unique=True)
    book_amount = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)


    class Meta:
        unique_together = ('author','title','genre',)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class BookRentHistory(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, editable=False, related_name='books')
    rent_date = models.DateField(auto_now_add=True, editable=False)
    back_date = models.DateField(
        default=datetime.now()+timedelta(days=30))

    @property
    def how_many_days(self):
        return str(self.back_date - datetime.now().date())[:2]



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
