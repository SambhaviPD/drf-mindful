from django.urls import path, include

from books.views import ListAddAuthorList, AuthorDetail, ListAddBookList, BookDetail

urlpatterns = [
    path('api/authors/', ListAddAuthorList.as_view(), name='authors'),
    path('api/authors/<uuid:pk>/', AuthorDetail.as_view(), name='author'),
    path('api/books/', ListAddBookList.as_view(), name='books'),
    path('api/books/<uuid:pk>/', BookDetail.as_view(), name="book"),
]
