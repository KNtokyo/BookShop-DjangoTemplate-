from django.db import models

from main.models import Book

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    phone = models.IntegerField()
    address = models.TextField()





