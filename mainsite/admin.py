from django.contrib import admin
from .models import Books
from .models import Book

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_author','book_summary')
class BookAdmin(admin.ModelAdmin):
    #list_display = ('chapter_id','chapter_name','chapter_content')
    list_display = ('chapter_id','chapter_name')

admin.site.register(Books,BooksAdmin)
admin.site.register(Book,BookAdmin)

