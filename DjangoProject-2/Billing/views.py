from django.shortcuts import render
from .forms import Ex4Form
from .models import Ex4Model
# Create your views here.

def index(request):

    if request.method == "POST":
        form = Ex4Form(request.POST)
        
        company =  request.POST.get('company') 
    
        print(company)

        mobile = request.POST.get('mobile')
        qun1 = request.POST.get('qun1')

        mqunt = 0
        if mobile != None:
            mqunt = qun1
        
        laptop = request.POST.get('laptop') 
        qun2 = request.POST.get('qun2')

        lqunt = 0
        if laptop!= None:
            lqunt = qun2

        total = int(mqunt)+int(lqunt)


        data = {
            "company": company,
            "mobile" : mqunt,
            "laptop" : lqunt,
            "total" : total
                        
        }


        
        context = {
            'data' : data
        }
        return render(request, 'ex4/bill.html', context)
    else:
        # form = Ex4Form()
        context = {
        }
        return render(request, 'ex4/index.html', context)


