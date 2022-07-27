from rest_framework import serializers

from books.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        read_only_fields = ('id',)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = ['id', 'title', 'description', 'rating', 'genre', \
            'numberofpages', 'willingtoshare', 'author']
        read_only_fields = ('id',)