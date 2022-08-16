from pkgutil import read_code
from django.contrib.auth.models import User
from rest_framework import serializers

from books.models import Author, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AuthorSerializer(serializers.ModelSerializer):
    addedBy = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'addedBy']
        read_only_fields = ('id',)

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=False)
    ownedBy = UserSerializer(many=False, read_only=True)

    class Meta:
        model= Book
        fields = ['id', 'title', 'description', 'rating', 'genre', \
            'numberofpages', 'willingtoshare', 'author', 'ownedBy']
        read_only_fields = ('id',)