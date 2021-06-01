
from django import forms
from django.forms import ModelForm, fields
from .models import Ex4Model

company_list = [
    ("HP", "HP"),
    ("Nokia", "Nokia"),
    ("Samsung", "Samsung"),
    ("Motorola", "Motorola"),
    ("Apple", "Apple")
]
type = [
    ("Mobile", "Mobile"),
    ("Laptop", "laptop")
]

class Ex4Form(ModelForm):
    class Meta:
        model = Ex4Model
        fields = '__all__'
        # company  = forms.ChoiceField(choices=company_list, widget=forms.RadioSelect())
        # widgets = {
        #     'company' : forms.ChoiceField(widget= forms.Select, ch),
        #     'type' : forms.RadioSelect()
        # }
