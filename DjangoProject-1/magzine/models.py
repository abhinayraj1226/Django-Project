from django.db import models

# Create your models here.
class Magzine(models.Model):
    Backround_Color = models.CharField(default=None, max_length=20)
    title_font_size = models.IntegerField(default=None)
    body_font_size = models.IntegerField(default=None)
    title_text = models.CharField(default=None, max_length=20)
    body_text = models.CharField(default=None, max_length=200)
    title_color = models.CharField(default=None, max_length=20)
    body_color  = models.CharField(default=None, max_length=20)
    image = models.ImageField(default=None, upload_to = "magzine/static/magzine/images/")

