from django.shortcuts import render
from work2.models import *

# Create your views here.
def einput(request):
    return render(request,'input.html')

def rajesh(request):
    id =int(request.GET['eid'])
    age =int(request.GET['eage'])
    name =request.GET['ename']
    salary =float(request.GET['esalary'])
    e =employee(eid=id, ename=name, eage=age, esalary=salary)
    e.save()
    return render(request,'link.html')

def display(request):
    data = employee.objects.all()
    return render(request,'display.html',{'records':data})