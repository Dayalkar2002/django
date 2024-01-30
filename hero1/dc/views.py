from django.shortcuts import render
from .models import Dc
from .forms import Ddc
# Create your views here.
def superman(request):
    context={'age':[1,2,3,4]}
    return render(request,'dc/superman.html',context,)

def batman(request):
    dc=Dc.objects.all()
    info=Ddc()
    return render(request,'dc/batman.html',{'dcs':dc,'check':info})
