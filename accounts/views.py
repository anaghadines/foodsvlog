from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email = request.POST['email']
        password1=request.POST['password']
        password2=request.POST['Re-type Password']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(firstname=firstname,lastname=lastname,username=username,email=email,password1=password1,password2=password2)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('register')
        return redirect('/')
    else:
         return render(request,'register.html')