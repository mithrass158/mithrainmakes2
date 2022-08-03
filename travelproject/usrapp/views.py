
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def login (request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')

    return render(request,"login.html")
def register (request):
    if request.method=='POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exist")
                return redirect ('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect ('register')
            else:
                user = User.objects.create_user(username=uname, password=password, first_name=fname, last_name=lname,
                                                email=email)

                user.save();
                print("user created")
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render (request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
