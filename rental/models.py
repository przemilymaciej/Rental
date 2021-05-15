from django.db import models
from django.utils import timezone

class Book(models.Model):
    whoAdd = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    ISBN = models.CharField(max_length=20, unique=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    borrowed = models.BooleanField(
        default=False)


    class Meta:
        unique_together = ('author','title','genre',)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Film(models.Model):
    whoAdd = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    director = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    length = models.DecimalField(max_digits=19, decimal_places=2)
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
    length = models.DecimalField(max_digits=19, decimal_places=2)
    borrowed = models.BooleanField(
        default=False)
    class Meta:
        unique_together = ('genre','tracks',)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
