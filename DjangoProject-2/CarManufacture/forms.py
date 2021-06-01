from .models import ex1
from django import forms
from django.forms import ModelForm

car_company = [('Tesla','Tesla'), ('BMW', 'BMW'), ('MAR','MAR'), ('Mahendra', 'Mahendra')]

class ex1Form(ModelForm):
    class Meta:
        model = ex1
        fields = '__all__'
        widgets = {
            'manufacture_company' : forms.Select(choices=car_company)
        }