from django.shortcuts import render
from .forms import CrForm
from .models import CrModel
# Create your views here.

def crud(request):
    cm=CrModel.objects.all()
    # cf=CrForm
    return render(request,'core/core.html',{'cm':cm})