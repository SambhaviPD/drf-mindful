import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Author, Book

# Create your tests here.

# CREATE AUTHOR
@pytest.mark.django_db
def test_is_valid_author_is_created():
    url = reverse('authors')
    data = {
        "name" : "Yann Martel",
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Author.objects.get().name == "Yann Martel"

# MISSING AUTHOR NAME
def test_author_name_missing_returns_bad_request():
    url = reverse("authors")
    data = {
        "country" : "Ireland"
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST

# RETRIEVE
@pytest.mark.django_db
def test_is_valid_author_returned():
    author = Author.objects.create(name="Margaret Atwood")
    url = reverse("author", args=[author.id])

    client = APIClient()
    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Margaret Atwood"

# RETRIEVE BOOKS BY A PARTICULAR AUTHOR
@pytest.mark.django_db
def test_books_by_corresponding_author():
    author = Author.objects.create(name="Sarah Morgan")
    one_more_author = Author.objects.create(name="Michio Kaku")

    book = Book.objects.create(title="Beach House Summer", \
        description="When Joanna Whitman's famous ex-husband dies in a car accident, she doesn't know what to feel. Their dysfunctional marriage held more painful secrets than she cares to remember. But when she discovers that the young woman with him in the crash is pregnant, Joanna feels compelled to act, knowing exactly how brutal the media spotlight will be on celebrity chef Cliff Whitman's ex-wife and his mysterious female friend.", \
        rating=4.10, \
        genre="Romance", \
        numberofpages=417, \
        willingtoshare=True
        )
    book.author.add(author)

    one_more_book = Book.objects.create(title="The God Equation: The Quest for a Theory of Everything", \
        description="When Joanna Whitman's famous ex-husband dies in a car accident, she doesn't know what to feel. Their dysfunctional marriage held more painful secrets than she cares to remember. But when she discovers that the young woman with him in the crash is pregnant, Joanna feels compelled to act, knowing exactly how brutal the media spotlight will be on celebrity chef Cliff Whitman's ex-wife and his mysterious female friend.", \
        rating=4.07, \
        genre="Nonfiction", \
        numberofpages=225, \
        willingtoshare=True
        )
    one_more_book.author.add(one_more_author)

    url = reverse("book", args=[book.id])
    client = APIClient()
    response = client.get(url)

    book = Book.objects.filter(author__id=response.data["author"][0])

    #assert Book.objects.filter(author__name) == "Sarah Morgan"


# LIST
@pytest.mark.django_db
def test_all_authors_returned():
    url = reverse("authors")
    Author.objects.create(name="Chantelle Atkins")
    Author.objects.create(name="Mark Dawson")
    
    client = APIClient()
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Chantelle Atkins"
    assert response.data[1]["name"] == "Mark Dawson"

# UPDATE
@pytest.mark.django_db
def test_author_name_changed():
    author = Author.objects.create(name="Sarah Morgan")

    url = reverse("author", args=[author.id])

    data = {
        "name" : "Michael Ko",
    }

    client = APIClient()
    response = client.put(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Michael Ko"


@pytest.mark.django_db
def test_author_name_unchanged_missing_data():
    author = Author.objects.create(name="Sarah Morgan")

    url = reverse("author", args=[author.id])

    data = {
        "country" : "Ireland"
    }

    client = APIClient()
    response = client.put(url, data=data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST

# PARTIAL UPDATE
@pytest.mark.django_db
def test_partial_update_book_detail():

    author = Author.objects.create(name="Sarah Morgan")

    book = Book.objects.create(
        title="Beach House Summer", \
        description="When Joanna Whitman's famous ex-husband dies in a car accident, she doesn't know what to feel. Their dysfunctional marriage held more painful secrets than she cares to remember. But when she discovers that the young woman with him in the crash is pregnant, Joanna feels compelled to act, knowing exactly how brutal the media spotlight will be on celebrity chef Cliff Whitman's ex-wife and his mysterious female friend.", \
        rating=4.10, \
        genre="Romance", \
        numberofpages=417, \
        willingtoshare=True
    )

    book.author.add(author)

    url = reverse("book", args=[book.id])

    data = {
        "numberofpages" : 420,
    }

    client = APIClient()

    response = client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["numberofpages"] == 420

@pytest.mark.django_db
def test_partial_update_incorrect_book_detail():

    author = Author.objects.create(name="Sarah Morgan")

    book = Book.objects.create(
        title="Beach House Summer", \
        description="When Joanna Whitman's famous ex-husband dies in a car accident, she doesn't know what to feel. Their dysfunctional marriage held more painful secrets than she cares to remember. But when she discovers that the young woman with him in the crash is pregnant, Joanna feels compelled to act, knowing exactly how brutal the media spotlight will be on celebrity chef Cliff Whitman's ex-wife and his mysterious female friend.", \
        rating=4.10, \
        genre="Romance", \
        numberofpages=417, \
        willingtoshare=True
    )

    book.author.add(author)

    url = reverse("book", args=[book.id])

    data = {
        "numberofpagesssss" : 420,
    }

    client = APIClient()

    response = client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK

# DELETE
@pytest.mark.django_db
def test_delete_author():
    author = Author.objects.create(name="Jess Owens")

    url = reverse("author", args=[author.id])

    client = APIClient()

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert len(Author.objects.all()) == 0