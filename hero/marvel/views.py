from django.shortcuts import render

# Create your views here.
def ironman(request):
    cont={'name':'manish'}
    return render(request,'marvel/index.html',cont)