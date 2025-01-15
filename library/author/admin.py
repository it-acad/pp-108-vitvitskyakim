from django.contrib import admin
from .models import Author, AuthorBook


class AuthorBookInline(admin.TabularInline):
    model = AuthorBook
    extra = 1  

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('name', 'id') 
    search_fields = ('name', 'surname', 'patronymic') 
    inlines = [AuthorBookInline]

admin.site.register(Author, AuthorAdmin)