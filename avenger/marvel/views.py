from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nav_bar(request):
    return render(request,'index.html')

def ironwomen(request):
    return HttpResponse("<b>iron women!!!")