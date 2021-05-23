from django.contrib import admin
from .models import Book
from .models import Film
from .models import CD
from .models import BookGenre
from .models import FilmGenre


admin.site.register(Book)
admin.site.register(Film)
admin.site.register(CD)
admin.site.register(BookGenre)
admin.site.register(FilmGenre)
# Register your models here.
