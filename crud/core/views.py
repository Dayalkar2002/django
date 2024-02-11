from django.shortcuts import render,redirect
from .forms import CrudForm
from .models import CrudModel
# Create your views here.
def core(request):
    if request.method=='POST':
        crud=CrudForm(request.POST)
        if crud.is_valid():
            # nm=crud.cleaned_data['name']
            # hn=crud.cleaned_data['heroic_name']
            # print('name:-',nm)
            # print('heroic_name:-',hn)
            # cf=CrudModel(name=nm,heroic_name=hn)
            crud.save()
        cm=CrudModel.objects.all() 
        cd=CrudForm()    

    else:
       cm=CrudModel.objects.all()
       cd=CrudForm()

    return render(request,'core/core.html',{'cd':cd,'cm':cm})


def delete(request,id):
    if request.method=='POST':
        mm=CrudModel.objects.get(pk=id)
        mm.delete()
    return redirect('/core/')
        

def update(request,id):
    if request.method=='POST':
        mm=CrudModel.objects.get(pk=id)
        mf=CrudForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()        

    else:
        mm=CrudModel.objects.get(pk=id)
        mf=CrudForm(instance=mm)

    return render(request,'core/update.html',{'mf':mf})            