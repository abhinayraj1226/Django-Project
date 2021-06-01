from django.shortcuts import render
from .forms import MagzineForm
from .models import Magzine
# Create your views here.

def index(request):
    form = MagzineForm()
    magz = Magzine()
    if request.method == 'POST':
        form = MagzineForm(request.POST, request.FILES)
        if form.is_valid:
            magz = form.save()
            magz.save()
        img = "magzine/images/"+request.FILES['image'].name
        context = {
        'img': img,
        'magzine': magz
        }
        return render(request, 'magzine/magzine.html', context)

    else:
        context = {
        'form': form
        }
        return render(request, 'magzine/index.html', context)
