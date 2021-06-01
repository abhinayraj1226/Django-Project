from django.db import models

# Create your models here.
class Ex3Model(models.Model):
    username = models.CharField(max_length= 20, blank=True)
    password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    contact = models.CharField(max_length =12)