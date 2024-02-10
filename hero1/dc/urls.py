from django.urls import path
from . import views

urlpatterns = [
    path('superman/',views.superman,name='superman'),
    path('',views.batman),
]
