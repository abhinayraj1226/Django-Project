from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 250, default=None)
    date_of_birth = models.DateField(default=None)
    address = models.CharField(max_length=250, default=None)
    phone = models.IntegerField()
    email = models.EmailField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    english = models.IntegerField()

