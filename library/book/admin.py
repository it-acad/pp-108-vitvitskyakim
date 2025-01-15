from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count', 'display_authors')
    list_filter = ('name', 'count', 'authors')
    search_fields = ('name', 'description', 'authors__name') 
    filter_horizontal = ('authors',)
    fieldsets = (
        ('Основна информация', {
            'fields': ('name', 'description', 'count'),
        }),
        ('Authors', {
            'fields': ('authors',),
        }),
    )

    def display_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    display_authors.short_description = "Authors" 

admin.site.register(Book, BookAdmin)