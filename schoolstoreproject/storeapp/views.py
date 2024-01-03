from django.contrib import messages,auth
from django.contrib.auth.models import User
from.models import Department
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    obj=Department.objects.all()
    return render(request,'index.html',{'result':obj})
#def login(request):
 #   if request.method == 'POST':
  #      username = request.POST['username']
   #     password = request.POST['password']
    #    user = auth.authenticate(username=username,password=password)
     #   if user is not None:
      #      auth.login(request,user)
       #     return  redirect('buttonpage')
       # else:
           # messages.info(request,"Invalid credentials")
            #return  redirect('register')
    #return render(request,"login.html")
#def register(request):
 #   if request.method == 'POST':
  #      username=request.POST['username']
   #     password=request.POST['password']
    #    confirmpassword=request.POST['confirmpassword']
     #   if password == confirmpassword:
      #      if User.objects.filter(username=username).exists():
       #         messages.info(request,"username taken")
       #         return redirect('register')
       #     else:
        #        user = User.objects.create_user(username=username,password=password)
         #       user.save();
      #  return redirect('/')
    #return render(request,"register.html")
def buttonpage(request):
    return render(request,"buttonpage.html")
def newpage(request):
    return render(request,"newpage.html")
#def logout(request):
 #   auth.logout(request)
  #  return redirect('/')
def order(request):
    return render(request,"order.html")
def computerscience(request):
    return render(request,"computerscience.html")
def mathematics(request):
    return render(request,"mathematics.html")
def physics(request):
    return render(request,"physics.html")
def humanities(request):
    return render(request,"humanities.html")
def commerce(request):
    return render(request,"commerce.html")
