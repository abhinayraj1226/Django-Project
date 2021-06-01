from django.shortcuts import render
from .models import Ex2Model
from .forms import Ex2Form

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Ex2Form(request.POST)
        if form.is_valid:
            ft = form.save()
            ft.save
            request.session['name'] = ft.name
            request.session['roll'] = ft.roll
            request.session['subject'] = ft.subject
        if request.session.has_key('name'):
            data = {
                'name' : request.session['name'],
                'roll' : request.session['roll'],
                'subject' : request.session['subject'],
            }
            context = {
                'data' : data
            }
            return render(request, 'ex2/secondPage.html', context)

    else:
        form = Ex2Form()
        context = {
            'form' : form
        }
        return render(request, 'ex2/firstPage.html', context)
