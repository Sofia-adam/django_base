from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a(request):
    return HttpResponse(" This is saturday work ")

def b(request):
    return HttpResponse("This is assignment1 on sat")

def c(request):
    return HttpResponse("Exteding the work")

def d(request):
    return HttpResponse("Practcing more to get perfect")
