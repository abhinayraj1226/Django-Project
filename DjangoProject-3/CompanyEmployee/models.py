from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
# Create your models here.
class WORKS(models.Model):
    person_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length = 20)
    salary = models.IntegerField()


class LIVES(models.Model):
    person_name = models.ForeignKey(WORKS, on_delete=CASCADE)
    street = models.CharField(max_length = 40)
    city = models.CharField(max_length = 20)


