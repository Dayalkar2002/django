from django.shortcuts import render,redirect
from . forms import SignUp
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def sign_up(request):
#     if request.method=='POST':
#         ss=UserCreationForm(request.POST)
#         if ss.is_valid():
#             ss.save()
#             return redirect('/signup/')
#     else:
#        ss=UserCreationForm()
#     return render(request,'core/signup.html',{'ss':ss})    


def sign_up(request):
    if request.method=="POST":
        ss=SignUp(request.POST)
        if ss.is_valid():
            ss.save()    
            return redirect('/signup/')
    else:
       ss=SignUp()
    return render(request,'core/signup.html',{'ss':ss})


def log_in(request):
    if not request.user.is_authenticated:    
        if request.method=="POST":
            af=AuthenticationForm(request=request,data=request.POST)
            if af.is_valid():
                name=af.cleaned_data['username']
                pas=af.cleaned_data['password']
                user=authenticate(username=name,password=pas)
                if user is not None:
                    login(request,user)
                    return redirect('/profile/')
        else:
            af=AuthenticationForm()
            return render(request,'core/login.html',{'af':af})
    else:
        return redirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html',{'name':request.user})
    else:
        return redirect('/login/')

def log_out(request):
    logout(request)
    return redirect('/login/')

