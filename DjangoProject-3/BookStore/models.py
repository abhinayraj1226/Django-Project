from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)

    def __str__(self):
        return self.email


class Publisher(models.Model):
    publisher_name = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    website = models.CharField(max_length = 20)

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    title = models.CharField(max_length = 20)
    publication_date = models.DateField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=CASCADE)
