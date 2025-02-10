from django.urls import path
from .views import ListBook

urlpatterns = [
    path('book_list/', ListBook.as_view(), name='book_list'),
]
