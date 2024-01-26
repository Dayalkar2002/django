from django.shortcuts import render

# Create your views here.
def navbar(request):
    return render(request,'flipkart/index.html')