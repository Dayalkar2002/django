from django.urls import path
from dc import views
urlpatterns = [
    path('superman/', views.superman),
    path('register/', views.register),
]
