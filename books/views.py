from django.shortcuts import render

from rest_framework import generics

from books.api.serializers import AuthorSerializer, BookSerializer
from books.models import Author, Book

# Create your views here.
class ListAddAuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        return serializer.save(addedBy=self.request.user)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListAddBookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save(ownedBy=self.request.user)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

