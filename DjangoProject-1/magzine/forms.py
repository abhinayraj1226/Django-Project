from django import forms
from django.forms import ModelForm
from .models import Magzine

COLOR_CHOICES= [
('black','black'),
('red','red'),
('yellow','yellow'),
('green','green'),
('white','white'),
('blue','blue')]

FONT_SIZE= [tuple([x,x]) for x in range(10,80,5)]

class MagzineForm(ModelForm):
    class Meta:
        model = Magzine
        fields = '__all__'
        widgets = {
                'Backround_Color' : forms.Select(choices=COLOR_CHOICES),
                'title_color' : forms.Select(choices=COLOR_CHOICES),
                'body_color' : forms.Select(choices=COLOR_CHOICES),
                'title_font_size' : forms.Select(choices=FONT_SIZE),
                'body_font_size' : forms.Select(choices=FONT_SIZE)
            }