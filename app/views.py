from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Book


# Create your views here.
class Mixin:
    def sort_queryset(self, queryset):
        return queryset.order_by('-year')


class ListBook(Mixin, ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    success_url = reverse_lazy('book_list')
    paginate_by = 3
    
    
    def get_queryset(self):
        qs = super().get_queryset()
        return self.sort_queryset(qs)
    
    
