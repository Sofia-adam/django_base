from django.shortcuts import render
from django.http import *


# Create your views here.
def fun1(request):
    return HttpResponse("This is my Project")

def fun2(request):
    return HttpResponse("Sample project was done....!")

def sample(request):
    context = {"name":"Rajesh junjuri",
               "place":"Hyd",
               "age":"22"}
    return render(request,"home.html",context)