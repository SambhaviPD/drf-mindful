import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from books.models import Author, Book

@pytest.fixture(scope="session")
def create_user():
    def _create_user():
        return User.objects.create_user("AdminUser", "sambhavi@golittlebig.com", "testpassword")

    return _create_user

@pytest.fixture(scope="session")
def create_authenticated_client():
    def _create_authenticated_client(user):
        client = APIClient()
        client.force_login(user)

        return client
    return _create_authenticated_client

@pytest.fixture(scope='session')
def create_book():

    def _create_book(name):
        
        author = Author.objects.create(name=name)

        book = Book.objects.create(
            title="Beach House Summer", \
            description="When Joanna Whitman's famous ex-husband dies in a car accident, she doesn't know what to feel. Their dysfunctional marriage held more painful secrets than she cares to remember. But when she discovers that the young woman with him in the crash is pregnant, Joanna feels compelled to act, knowing exactly how brutal the media spotlight will be on celebrity chef Cliff Whitman's ex-wife and his mysterious female friend.", \
            rating=4.10, \
            genre="Romance", \
            numberofpages=417, \
            willingtoshare=True
        )

        book.author.add(author)

    return _create_book


