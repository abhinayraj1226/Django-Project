from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.
def index(request):
    form = ProductForm()
    product = Product.objects.all()
    if request.method == "POST":
        form1 = ProductForm(request.POST)
        if form1.is_valid:
            ftmp = form1.save()
            ftmp.save
        context = {
            'form': form,
            'product' : product

        }
        return render(request, 'ex4/index.html', context)

    if request.method == "GET":
        context = {
            'form' : form,
            'product' : product
        }
    return render(request, 'ex4/index.html', context)