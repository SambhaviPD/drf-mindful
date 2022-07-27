from django.urls import path, include
from rest_framework import routers

from books.api.viewsets import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('api/', include(router.urls)),
]
