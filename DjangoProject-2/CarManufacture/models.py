from django.db import models

# Create your models here.
class ex1(models.Model):
    manufacture_company = models.CharField(max_length=20)
    models_name = models.CharField(max_length = 20)