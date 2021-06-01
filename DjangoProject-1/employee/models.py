from django.db import models

# Create your models here.
class Employee(models.Model):
    date_of_birth = models.DateField()
    employee_id = models.IntegerField(default=None)
    