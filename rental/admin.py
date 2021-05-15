from django.contrib import admin
from .models import Book
from .models import Film
from .models import CD

admin.site.register(Book)
admin.site.register(Film)
admin.site.register(CD)
# Register your models here.
