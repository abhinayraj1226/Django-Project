from django.forms.widgets import SelectMultiple, TextInput
from .models import Author, Publisher, Book
from django.forms import ModelForm,DateInput
from django import forms
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    
class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'publication_date' : DateInput(attrs={ 'type' : 'date'})
        }