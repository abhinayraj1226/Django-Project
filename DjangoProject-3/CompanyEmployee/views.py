from django.shortcuts import render
from .models import WORKS, LIVES
from .forms import EmployeeDetailForm, AddressForm

# Create your views here.
def index(request):
    return render(request, "ex2/index.html")

def addEmployee(request):

    if request.method == "POST":
        emplyeeform = EmployeeDetailForm(request.POST)
        addressform = AddressForm(request.POST, emplyeeform)

        if emplyeeform.is_valid and addressform.is_valid:
            emp = emplyeeform.save()
            addForm = addressform.save(commit=False)
            addForm.person_name = emp
            addForm.save()
        
        context = {
            'form1': emplyeeform,
            'form2' : addressform,
            'dataFilled' : True

        }
        return render(request, 'ex2/addEmployee.html', context)



    elif request.method == "GET":
        emplyeeform = EmployeeDetailForm()
        addressform = AddressForm()

        context = {
            'form1': emplyeeform,
            'form2' : addressform

        }
        return render(request, 'ex2/addEmployee.html', context)
    else :
        return render(request, 'ex2/index.html')


def findEmployee(request):
    if request.method == "POST":
        company = request.POST.get('company')
        empl = WORKS.objects.filter(company_name = company)
        hasData = False

        if len(empl) > 0:
            hasData = True
        addr = []
        for data in empl:
            tmp = LIVES.objects.get(person_name = data)
            addr.append(tmp)
        dtl = zip(empl, addr)
        context = {
            'empl' : dtl,
            'hasData' : hasData
            
        }
        
        return render(request, 'ex2/showEmployeeByCompany.html', context)
        
    elif request.method == "GET":
        context = {
                    'empl' : -1
                }
        return render(request, 'ex2/showEmployeeByCompany.html', context)
    else:
        return render(request, 'ex2/index.html')