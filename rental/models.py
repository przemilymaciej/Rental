from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models import Count
from django.core.exceptions import ValidationError

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
        max_length=50,
        help_text="Enter a film genre"
    )
    slug = models.SlugField(unique=True)

    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FilmGenre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "FilmGenres"



class Film(models.Model):
    director = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    genre = models.ForeignKey('FilmGenre', on_delete=models.PROTECT, null=True)
    length = models.DecimalField(max_digits=3, decimal_places=2)
    film_amount = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('director', 'title', 'length',)

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        genres = FilmGenre.objects.annotate(num_films=Count('film')).order_by('-num_films')
        if genres:
            diff = Film.objects.filter(genre=self.genre).count() - genres[0].num_films
            if diff > 3 :
                raise ValidationError(_('Liczby roznych filmow danego gatunku w ramach calej kolekcji moga roznic sie o 3!'))
        super(Film, self).clean(*args, **kwargs)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.full_clean()
        super(Film, self).save(*args, **kwargs)



class FilmRentHistory(models.Model):
    film = models.ForeignKey(
        Film, on_delete=models.PROTECT, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, editable=False, related_name='films')
    rent_date = models.DateField(auto_now_add=True, editable=False)
    back_date = models.DateField(
        default=datetime.now()+timedelta(days=30))

    @property
    def how_many_days(self):
        return str(self.back_date - datetime.now().date())[:2]


class CDGenre(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a CD genre"
    )
    slug = models.SlugField(unique=True)

    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CDGenre, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "CDGenres"



class CD(models.Model):
    band = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    genre = models.ForeignKey('CDGenre', on_delete=models.PROTECT, null=True)
    length = models.DecimalField(max_digits=3, decimal_places=2)
    CD_amount = models.IntegerField(default=0)
    tracks = models.TextField(max_length=300)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        ct = CD.objects.filter(genre=self.genre).filter(tracks=self.tracks).count()
        if ct:
            if ct > 1:
                 raise ValidationError(
                        'w ramach jednego gatunku nie możemy oferować dwóch płyt o tej samej liście utworów')

        mydiscog = CD.objects.filter(band=self.band).values('genre').distinct().count()
        if mydiscog:
            if mydiscog > 2:
                 raise ValidationError('płyty danego zespołu mogą być oferowane tylko w dwóch gatunkach!')
        super(CD, self).clean(*args, **kwargs)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.full_clean()
        super(CD, self).save(*args, **kwargs)



class CDRentHistory(models.Model):
    cd = models.ForeignKey(
        CD, on_delete=models.PROTECT, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, editable=False, related_name='CDs')
    rent_date = models.DateField(auto_now_add=True, editable=False)
    back_date = models.DateField(
        default=datetime.now()+timedelta(days=30))

    @property
    def how_many_days(self):
        return str(self.back_date - datetime.now().date())[:2]



# Create your models here.
