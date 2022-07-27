from django.db import models

# Create your models here.
import uuid

from django.db import models

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    GENRE_CHOICES = [
        ('CHICK-LIT', 'Chick-lit'),
        ('CHILDREN''S', 'Children''s'),
        ('COMICS', 'Comics'),
        ('CRIME', 'Crime'),
        ('FANTASY', 'Fantasy'),
        ('MANGA', 'Manga'),
        ('MYSTERY', 'Mystery'),
        ('NONFICTION', 'Nonfiction'),
        ('ROMANCE', 'Romance'),
        ('SELFHELP', 'Self Help'), 
        ('SUSPENSE', 'Suspense'),
        ('THRILLER', 'Thriller'),
        ('YOUNGADULT', 'Young Adult'),
        ('OTHER', 'Other')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, \
        default='OTHER')
    numberofpages = models.PositiveSmallIntegerField()
    willingtoshare = models.BooleanField(default=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title + ' written by ' + self.author}"