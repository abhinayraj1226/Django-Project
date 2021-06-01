from django.shortcuts import render
from .forms import Ex3Form
from .models import Ex3Model
# Create your views here.

def index(request):

    if request.method == "POST":
        form = Ex3Form(request.POST)
        data = Ex3Model()
        if form.is_valid:
            data = form.save()
            data.save
        
        context = {
            'data' : data
        }
        return render(request, 'ex3/home.html', context)
    else:
        form = Ex3Form()
        context = {
            'form' : form
        }
        return render(request, 'ex3/register.html', context)


