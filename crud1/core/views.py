from django.shortcuts import render
# Create your views here.
from . forms import SignUp

def user(request):
    if request.method=="POST":
        ss=SignUp(request.POST)
        if ss.is_valid:
            ss.save()
        ss=SignUp()    

    else:
       ss=SignUp()
    return render(request,'core/core.html',{'ss':ss})