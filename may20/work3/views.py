from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')

def adds(request):
    aa = int(request.POST['fn'])
    bb = int(request.POST['ln'])
    cc = aa + bb
    return HttpResponse("the sum is:"+str(cc))
    