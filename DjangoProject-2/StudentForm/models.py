from django.db import models

# Create your models here.
class Ex2Model(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(max_length = 5)
    subject = models.CharField(max_length = 20)
