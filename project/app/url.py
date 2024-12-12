from django.urls import path
from.import views
urlpatterns =[
    path('',views.register),
    path('',views.userhome),
]