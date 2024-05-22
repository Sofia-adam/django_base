from django.shortcuts import render
from django.http import HttpResponse
from time import ctime

# Create your views here.
def time(request):
    mycdt = ctime()
    return HttpResponse("The current time is : {}".format(mycdt))

