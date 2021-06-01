from django.shortcuts import render
from django.utils import timezone
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def index(request):
    form = EmployeeForm()
    empl = Employee()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid:
            empl = form.save()
            empl.save()
        # year = timezone.now().year
        # y1 = empl.date_of_birth.year
        rt =  timezone.now().year - empl.date_of_birth.year
        elgb = False
        if rt > 5:
            elgb = True

        context = {
        'eligible' : elgb,
        'form': form,
        }
        return render(request, 'employee/index.html', context)

    else:
        context = {
        'form': form,
        }
        return render(request, 'employee/index.html', context)
