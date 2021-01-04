from django.shortcuts import render
from django.db.models import Q

from main.models import Book, Genre, Author


def index(request):
    genres = Genre.objects.all()
    return render(request, 'index.html', {'genres': genres})

def book_list(request, slug):
    book_list = Book.objects.filter(genre__slug=slug)
    return render(request, 'book_list.html', {'books': book_list})

def author_detail(request, pk):
    author = Author.objects.get(id=pk)
    author_books = author.books.all()
    return render(request, 'author_detail.html', {'author': author, 'author_books': author_books})