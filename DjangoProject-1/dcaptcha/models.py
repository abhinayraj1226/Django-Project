from django.db import models

# Create your models here.

class Dcaptcha(models.Model):
    num = models.CharField(max_length=30, default=None)