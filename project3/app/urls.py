from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('',views.register),
    path('home',views.home),
    path('logout',views.logout),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
]