from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid details")
            return redirect('login')
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        uname=request.POST['user']
        fname=request.POST['first']
        lname = request.POST['last']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                details=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                details.save()
                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
    # return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')