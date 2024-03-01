from django.shortcuts import render
from .forms import CrForm
from .models import CrModel
# Create your views here.

def crud(request):
    if request.method=="POST":
        crud=CrForm(request.POST)
        if crud.is_valid():
            nm=crud.cleaned_data['name']
            hn=crud.cleaned_data['heroic_name']
            print('name',nm)
            print('heroic_name',hn)
            mm=CrModel(name=nm,heroic_name=hn)
            mm.save()
        cm=CrModel.objects.all()
        cf=CrForm()
    else:
        cm=CrModel.objects.all()
        cf=CrForm()
    return render(request,'core/core.html',{'cm':cm},{"cf":cf})