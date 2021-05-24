from django.contrib import admin
from .models import Book
from .models import BookRentHistory
from .models import BookGenre



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
