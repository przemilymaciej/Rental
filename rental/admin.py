from django.contrib import admin
from .models import Book
from .models import BookRentHistory
from .models import BookGenre
from .models import Film
from .models import FilmRentHistory
from .models import FilmGenre
from .models import CD
from .models import CDRentHistory
from .models import CDGenre



@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'book_amount', 'genre',
              'ISBN')

    list_display = ('title', 'author', 'genre', 'ISBN', 'book_amount', 'popularity')



@admin.register(BookRentHistory)
class BookRentHistoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rent_date','back_date')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FilmGenre)
class FilmGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', )


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ('director', 'title', 'genre', 'length',
              'film_amount')

    list_display = ('director', 'title', 'genre', 'length',
              'film_amount', 'popularity')



@admin.register(FilmRentHistory)
class FilmRentHistoryAdmin(admin.ModelAdmin):
    list_display = ('film', 'user', 'rent_date','back_date')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(CDGenre)
class CDGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', )


@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    fields = ('band','title', 'genre', 'length',
              'CD_amount','tracks')

    list_display = ('band','title', 'genre', 'length',
              'CD_amount','tracks', 'popularity')



@admin.register(CDRentHistory)
class CDRentHistoryAdmin(admin.ModelAdmin):
    list_display = ('cd', 'user', 'rent_date','back_date')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False