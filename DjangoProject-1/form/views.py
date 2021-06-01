from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse

from .models import Student

from .forms import StudentForm

# Create your views here.

def index(request):
    form = StudentForm()
    student = Student()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # student.user = request.user # Set the user object here
            student.save()
            # return redirect('/st')
        form1 = StudentForm()
        percent = int((int(student.english) + int(student.chemistry) + int(student.physics))/300*100)
        context = {
            'percent': percent,
            'form': form1,
            'student' : student
        }
        return render(request, 'form/index.html', context)

    else:
        context = {
        'form': form,
        }
        
        return render(request, 'form/index.html', context)

