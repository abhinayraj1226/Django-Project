from django.shortcuts import render
from .forms import ArithmeticForm
from .models import Arithmetic
# Create your views here.

def index(request):
    form = ArithmeticForm()
    arth = Arithmetic()
    if request.method == 'POST':
        form = ArithmeticForm(request.POST)
        if form.is_valid:
            arth = form.save()
            arth.save()
        a = 0
        if(arth.operations == '+'):
            a = arth.input1 + arth.input2
        elif(arth.operations == '-'):
            a = arth.input1 - arth.input2
        elif(arth.operations == '*'):
            a = arth.input1 * arth.input2
        else:
            a = arth.input1 / arth.input2

        context = {
        'result' : a,
        'form': form
        }
        return render(request, 'arithmetic/index.html', context)

    else:
        context = {
        'form': form
        }
        return render(request, 'arithmetic/index.html', context)
