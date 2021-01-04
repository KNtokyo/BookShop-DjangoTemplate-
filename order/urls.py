from django.contrib import admin
from django.urls import path, include

from .views import create_order

urlpatterns = [
    path('<int:book_id>', create_order, name='create-order'),  #orders/
]