from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else :
            return render(request,'account/login.html')
            
    return render(request,'account/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"].lower()
        last_name=request.POST["last_name"].lower()
        email = request.POST["email"].lower()
        username=request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["c_password"]

        if User.objects.filter(email=email).exists():
            messages.info(request,'User alredy exists')
        elif password != password2:
             messages.info(request,'password does not match')
        else:
            user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
            user.save()
            return redirect('/account')
    else:
        return render(request,'account/signup.html')