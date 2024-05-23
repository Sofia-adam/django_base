from django.shortcuts import render
from work1.forms import *

# Create your views here.
def input(request):
    obj=student()
    return render (request,'input.html',{'sform':obj})