from django.urls import path
from marvel import views
urlpatterns = [
    path('nav-bar/', views.nav_bar),
    path('ironwomen/', views.ironwomen),
]