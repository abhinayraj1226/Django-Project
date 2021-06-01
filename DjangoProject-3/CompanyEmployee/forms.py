from django.forms import ModelForm
from .models import WORKS, LIVES


class EmployeeDetailForm(ModelForm):
    class Meta:
        model = WORKS
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = LIVES
        fields = ['street', 'city']

    