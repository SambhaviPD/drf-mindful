import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Author, Book

# Create your tests here.

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

def test_author_name_missing_returns_bad_request():
    url = reverse("authors")
    data = {
        "country" : "Ireland"
    }
    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_is_valid_author_returned():
    url = reverse("authors")
    data = {
        "uuid" : "604a0cb8-056e-4bc0-9941-6c0a90e8d403"
    }
    client = APIClient()
    response = client.get(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_all_authors_returned():
    url = reverse("authors")
    client = APIClient()
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK