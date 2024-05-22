from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getin(request):
    return render(request,'getinput.html')

def postin(request):
    return render(request,'postinput.html')

def additions(request):
    if request.method == 'POST':
        a1 = int(request.POST['fn'])
        b1 = int(request.POST['sn'])
        c1 = a1+b1
        return render(request,'postresult.html',{'res':c1, 'num1':a1, 'num2':b1})
    
    elif request.method == 'GET':
        a1 = int(request.GET['fn'])
        b1 = int(request.GET['sn'])
        c1 = a1+b1
        return render(request,'getresult.html',{'res':c1, 'num1':a1, 'num2':b1})