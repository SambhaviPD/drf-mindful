from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from books.api.serializers import AuthorSerializer, BookSerializer
from books.models import Author, Book

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=False, methods=['DELETE'], url_path='delete-duplicate-authors', \
        url_name='delete-duplicate-authors')
    def delete_duplicate_authors(self, request):
        for row in Author.objects.all().reverse():
            if Author.objects.filter(name=row.name).count() > 1:
                row.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer