from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Book
from order.forms import CreateOrderForm
from order.models import Order


def create_order(request, book_id):
    book = Book.objects.get(id=book_id)
    books = Book.objects.exclude(id=book_id)
    order_form = CreateOrderForm(request.POST)
    print(order_form.is_valid())
    print(request.POST)
    if order_form.is_valid():
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save()
        return redirect(book.get_absoulute_url())
    return render(request, 'order.html', {'form': order_form, 'book': book, 'books': books})
