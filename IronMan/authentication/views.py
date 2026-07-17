from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "UserName already Exists")
            return redirect("sign_up")
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        messages.success(request, "Account Created Sucessfully.")
        return redirect("login")
    return render(request, "sign_up.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("emp_list")
        else:
            messages.error(request, "Invalid Username or Password.")
    return render(request,"login.html")