from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
    path('pcf/',views.pcf,name='pcf'),


]
