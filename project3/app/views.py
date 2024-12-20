from django.shortcuts import render,redirect
from .models import *

# Create your views here.
ad_us='admin'
ad_psw='admin@123'
def adminlogin(request):
    if request.method=='POST':
        adm_us=request.POST['username']
        adm_psw=request.POST['password']
        if ad_us==adm_us and ad_psw==adm_psw:
            return redirect(adminhome)
    return render(request,'admin/adminlogin.html')
def adminhome(request):
    emps=employee.objects.all()
    deps=departments.objects.all()
    if request.method=='POST':
        dep=request.POST['d']
        deppk=departments.objects.get(pk=dep)
        emps=employee.objects.filter(dname=deppk)
    return render(request,'admin/adminhome.html',{'deps':deps,'emps':emps})

def register(request):
    department=departments.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        dep=request.POST['d']
        current_dep=departments.objects.get(pk=dep)
        data=employee.objects.create(name=name,email=email,username=username,password=password,dname=current_dep)
        data.save()
        return redirect(login)
    return render(request,'user/register.html',{'deps':department})
        

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        data=employee.objects.all()
        for i in data:
            if i.username==username and i.password==password:
                print(i)
                request.session['userlog']=i.email
                return redirect(home)
    return render(request,'user/userlogin.html')
def home(request):
    if 'userlog' in request.session:
        return render(request,'user/userhome.html')
    else:
        return redirect(login)
    
def logout(request):
    if 'userlog' in request.session:
        del request.session['userlog']
        return redirect(login)
    else:
        return redirect(login)