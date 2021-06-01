from django.shortcuts import render,HttpResponse
import random
from .models import Dcaptcha
# Create your views here.

current_captcha = ""
no_of_try = 0
def createCaptcha():
    global current_captcha
    num=random.randrange(1121,9899)
    str_num=str(num)
    current_captcha = str_num
    return str_num

def index(request):
    global current_captcha,no_of_try
    if request.method == "POST":
        cap=request.POST.get("captha")
        if str(cap) == current_captcha :
            num = createCaptcha()
            context = {
            'img': num,
            'check' : True,
            'msg' : "Captcha Match!"
            }
            return render(request, 'dcaptcha/index.html', context)
        else:
            no_of_try = no_of_try+1
            num = createCaptcha()
            context = {
            'img': num,
            'data' : no_of_try,
            'msg' : "Not Matched!"
            }
            return render(request, 'dcaptcha/index.html', context)
    else:
        num = createCaptcha()
        context = {
        'img': num
        }
        return render(request, 'dcaptcha/index.html', context)
        
        

