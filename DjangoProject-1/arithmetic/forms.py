from django import forms
from django.forms import ModelForm,DateInput
from .models import Arithmetic

OPERATION_CHOICES= [('+','+'),
('-','-'),
('*','*'),
('/','/')]

class ArithmeticForm(ModelForm):
    class Meta:
        model = Arithmetic
        fields = '__all__'
        widgets = {
                'operations' : forms.Select(choices=OPERATION_CHOICES)
            }