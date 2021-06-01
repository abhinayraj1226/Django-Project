from django import forms
from django.forms import ModelForm,DateInput
from .models import Employee

INTEGER_CHOICES= [tuple([x,x]) for x in range(101,109)]

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # opt = forms.IntegerField(label="Select Employee ID:", widget=)
        widgets = {
                'date_of_birth': DateInput(attrs={'type': 'date'}),
                'employee_id' : forms.Select(choices=INTEGER_CHOICES)
            }