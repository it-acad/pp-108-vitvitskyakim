from django.shortcuts import render, redirect,get_object_or_404
from .models import Author
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def is_librarian(user):
    return user.role == 1

@user_passes_test(is_librarian)
def author_list(request):
    authors = Author.get_all()
    return render(request, 'author/author_list.html', {'authors': authors})
from django.shortcuts import render, redirect
from .models import Author


@user_passes_test(is_librarian)
def add_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")
        
        book_name = request.POST.get("book_name")
        book_description = request.POST.get("book_description")
        book_count = request.POST.get("book_count",10)

        author = Author.create(name=name, surname=surname, patronymic=patronymic)
        if book_name and book_description:
            book = Book.create(name=book_name, description=book_description, count=book_count)
            author.books.add(book)
        
        return redirect('author_list')

    return render(request, 'author/add_author.html')

@user_passes_test(is_librarian)
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    
    if author.books.exists():
        messages.error(request, "The author cannot be deleted because they have attached books.")
        return redirect('author_list')  

    author.delete()

    messages.success(request, "The author has been successfully deleted.")
    return redirect('author_list')
