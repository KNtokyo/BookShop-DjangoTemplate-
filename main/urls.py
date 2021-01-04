from django.contrib import admin
from django.urls import path, include

from main.views import index, book_list, author_detail

urlpatterns = [
    path('', index, name='home'),
    path('listing/<str:slug>/', book_list, name='books-listing'),
    path('author/<int:pk>/', author_detail, name='author-detail'),
]