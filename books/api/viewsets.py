from rest_framework.viewsets import ModelViewSet

from books.api.serializers import AuthorSerializer, BookSerializer
from books.models import Author, Book

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer