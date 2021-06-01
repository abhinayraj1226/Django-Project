from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length = 50)