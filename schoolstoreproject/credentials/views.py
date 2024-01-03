from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
#from django.contrib.auth.models import Abstractuser,User
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exits():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
                print("user created")
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('login')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('buttonpage')
        else:
            messages.info(request,"Invalid credentials")
            return  redirect('register')
    return render(request,"login.html")
