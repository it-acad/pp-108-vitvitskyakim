from django.contrib import admin
from .models import Author

from django.contrib import admin
from .models import Author, AuthorBook

class AuthorBookInline(admin.TabularInline):
    model = AuthorBook
    extra = 1 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    search_fields = ('name', 'surname')
    fieldsets = (
        ("Main INFO", {
            'fields': ('name', 'surname', 'patronymic'),
        }),
    )
    inlines = [AuthorBookInline] 

admin.site.register(Author, AuthorAdmin)