from django.shortcuts import render
from .models import Dc
from .forms import Ddc
# Create your views here.
def superman(request):
    context={'age':[1,2,3,4]}
    return render(request,'dc/superman.html',context,)

def batman(request):
    if request.method=="POST":
        info=Ddc(request.POST)
        if info.is_valid():
            nm=info.cleaned_data['name']
            hn=info.cleaned_data['heroic_name']
            print('Name:-',nm)
            print('heroic-name:-',hn)
            mm=Dc(name=nm,heroic_name=hn)
            mm.save()
    else:
        info=Ddc() 

    dc=Dc.objects.all()
    # info=Ddc()
    return render(request,'dc/batman.html',{'dcs':dc,'check':info})
