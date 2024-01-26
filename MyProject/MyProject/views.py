from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("<b>Hello World!!</b>")

def course(request,course):
    return HttpResponse(course)