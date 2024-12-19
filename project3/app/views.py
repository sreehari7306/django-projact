from django.shortcuts import render

# Create your views here.

def register(requst):
    department=department.objects.all()
    if requst.method=='post':
        name=requst.post['name']
        email=requst.post['email']
        username=requst.post['username']
        password=requst.post['password']
        dep=requst.post['d']
        current_dp=department.objects.get(pk=dep)
        data=employee.objects.create(name=name,email=email,password=password,username=username,)
        data.save()
        return redirect(login)
    return render(request,'user/register.html',{'deps':departments})

def userhome(request):
    emps=employee.objects.all()