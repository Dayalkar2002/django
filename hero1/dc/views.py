from django.shortcuts import render
from .models import Dc
# Create your views here.
def superman(request):
    context={'age':[1,2,3,4]}
    return render(request,'dc/superman.html',context)

def batman(request):
    dc=Dc.objects.all()
    return render(request,'dc/batman.html',{'dcs':dc})
