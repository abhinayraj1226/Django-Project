from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    visit = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE)
    title = models.CharField(max_length = 20)
    url = models.CharField(max_length = 50)