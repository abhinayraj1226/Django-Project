from django.shortcuts import render
from .models import Category, Page
from .forms import CategoryForm, PageForm
# Create your views here.
category = Category.objects.all()
form = CategoryForm()
def index(request):
    
    if request.method == "GET":
        
        context = {
            'form' : form,
            'category': category
        }
    return render(request, "ex1/index.html", context)


def page(request, cname):

    if request.method == "POST":
        category = Category.objects.get(name=cname)
        category.likes = int(category.likes)+1
        category.save()
        context = {
            'form' : form,
            'category': category
        }
        return render(request, "ex1/index.html", context)


    if request.method == "GET":
        category = Category.objects.get(name=cname)
        category.visit = int(category.visit)+1
        category.save()
        page = Page.objects.filter(category=category)
        context = {
            'page':page,
            'cname':cname
        }
        return render(request, "ex1/page.html", context)
