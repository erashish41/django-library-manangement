from django.shortcuts import render
from django.views.generic import ListView, CreateView
from library.models import IssuedBook, Member, Book, Author, Publisher, Category, LibraryBranch, City
# Create your views here.


class BookList(ListView, CreateView):
    model = Book
    