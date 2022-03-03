from django.contrib import admin

from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
