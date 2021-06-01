from django.db import models

# Create your models here.
class Ex4Model(models.Model):
    company = models.CharField(max_length=20)
    type = models.CharField(max_length = 20)
    quantity = models.IntegerField(max_length = 5)