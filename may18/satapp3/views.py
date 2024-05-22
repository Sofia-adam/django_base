from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from calendar import HTMLCalendar

# Create your views here.
def dmy(request):
    cyear = date.today().year
    cmonth = date.today().month
    h = HTMLCalendar()
    result = h.formatmonth(cyear,cmonth)
    return HttpResponse(result)