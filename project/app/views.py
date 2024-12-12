from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data=user.objects.all()
        for i in data:
            if i.email==email and i.password==password:
                print('loggedin')
                request.session['userlog']=i.email
                return redirect(userhome)
    return render(request,'user/userlogin.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=user.objects.create(name=name,email=email,password=password)
        data.save()
    return render(request,'user/register.html')

def userhome(request):
    if 'userlog' in request.session:
        return render(request,'user/userhome.html')
    else:
        return redirect(userlogin)

def logout(requset):
    if 'userlog' in requset.session:
        del requset.session['userlog']
        return redirect(userlogin)
    else:
        return redirect(userlogin)