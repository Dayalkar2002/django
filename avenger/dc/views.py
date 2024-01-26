from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def superman(request):
    return HttpResponse("<b>Spider Man!!!")

def register(request):
    return render(request,'table.html')