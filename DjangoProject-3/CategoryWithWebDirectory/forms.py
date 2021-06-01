from .models import Category, Page
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = '__all__'