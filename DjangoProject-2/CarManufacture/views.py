from django.shortcuts import render, resolve_url
from .forms import ex1Form
from .models import ex1

from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        ex1form = ex1Form(request.POST)
        if ex1form.is_valid:
            dt = ex1form.save()
            dt.save
            car_manufacture = dt.manufacture_company
            model_name = dt.models_name
            request.session['car_manufacture'] = car_manufacture
            request.session['model_name'] = model_name
        if request.session.has_key('car_manufacture'):
            car_manufacture = request.session['car_manufacture']
            model_name = request.session['model_name']
        data = {
            "car" : car_manufacture,
            "model" : model_name
        }
        context = {
            'data':data
        }
        return render(request, 'ex1/secondpage.html', context)

    else:
        ex1form = ex1Form()
        context = {
            'form' : ex1form
        }
        return render(request, 'ex1/index.html', context)

