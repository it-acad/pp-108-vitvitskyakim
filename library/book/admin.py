from django.contrib import admin
from .models import Book
from author.models import AuthorBook

class AuthorBookInline(admin.TabularInline):
    model = AuthorBook
    extra = 1

class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'count')
    search_fields = ('name',)

    fieldsets = (
        ("Main Info", {
            'fields': ('name', 'publication_year'),
        }),
        ("Changeable Info", {
            'fields': ('release_date',),
        }),
    )

    inlines = [AuthorBookInline]

admin.site.register(Book, BookAdmin)
