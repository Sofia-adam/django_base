from django.shortcuts import render
from time import ctime 

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def date(request):
    c = ctime()
    msg = "The current system date and time is: "+c
    return render(request,'welcome.html',{'message':msg})