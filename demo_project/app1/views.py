from django.shortcuts import render
from app1.forms import student

# Create your views here.
def hero(request):
    obj = student(request.POST)
    return render(request,'input.html',{'sform':obj})

def heroien(request):
    return render(request, 'log.html')