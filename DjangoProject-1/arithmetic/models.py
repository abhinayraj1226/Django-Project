from django.db import models

# Create your models here.
class Arithmetic(models.Model):
    input1 = models.IntegerField(default=None)
    input2 = models.IntegerField(default=None)
    operations = models.CharField(default = None, max_length=20)
    