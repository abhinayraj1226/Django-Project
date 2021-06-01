from .models import Ex2Model
from django.forms import ModelForm, widgets
from django import forms

subject_list = [('Java', 'Java'), ('Nodejs', 'Nodejs'),('Mongodb', 'Mongodb'),('Spring', 'Spring'),('Express', 'Express')]


class Ex2Form(ModelForm):
    class Meta:
        model = Ex2Model
        fields = '__all__'

        widgets = {
            'subject': forms.Select(choices=subject_list)
        }


