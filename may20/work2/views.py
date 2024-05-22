from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def a(request):
    return render(request,'sample.html')

def addition(request):
    a = int(request.GET['fn'])
    b = int(request.GET['ln'])
    c = a+b
    return HttpResponse("The sum is:" +str(c))