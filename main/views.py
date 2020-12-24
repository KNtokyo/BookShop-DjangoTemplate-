from django.shortcuts import render

from main.models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})
