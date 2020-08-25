from django.contrib import admin

from .models import Book, Opinion, Author


admin.site.register(Book)
admin.site.register(Opinion)
admin.site.register(Author)