
from django.forms import ModelForm, fields
from .models import Ex3Model
class Ex3Form(ModelForm):
    class Meta:
        model = Ex3Model
        fields = '__all__'