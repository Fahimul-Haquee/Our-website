from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse

# হোম পেজ
def home(request):
    return render(request, 'accounts/home.html')

# রেজিস্ট্রেশন ফাংশন
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists!"})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return JsonResponse({"message": "User registered successfully!"})
    return render(request, 'accounts/register.html')

# লগইন ফাংশন
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful!"})
        else:
            return JsonResponse({"error": "Invalid credentials!"})
    return render(request, 'accounts/login.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse

def home(request):
    return render(request, 'accounts/home.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists!"})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return JsonResponse({"message": "User registered successfully!"})
    return render(request, 'accounts/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful!"})
        else:
            return JsonResponse({"error": "Invalid credentials!"})
    return render(request, 'accounts/login.html')
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

# রেজিস্ট্রেশন ভিউ
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # চেক করা হচ্ছে ইউজার নাম আগে থেকেই আছে কি না
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists!"})

        # নতুন ইউজার তৈরি করা
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()

        # রেজিস্ট্রেশন সফল হলে লগইন করানো
        return JsonResponse({"message": "User registered successfully!"})

    return render(request, 'accounts/register.html')

# লগইন ভিউ
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # ইউজারের তথ্য যাচাই করা
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # ইউজারকে লগইন করা
            return redirect('welcome')  # লগইন সফল হলে ওয়েলকাম পেজে নিয়ে যাওয়া
        else:
            return JsonResponse({"error": "Invalid credentials!"})

    return render(request, 'accounts/login.html')

# ওয়েলকাম পেজ ভিউ
def welcome_page(request):
    return render(request, 'accounts/welcome.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirect to welcome page
        else:
            return JsonResponse({"error": "Invalid credentials!"})
    return render(request, 'accounts/login.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists!"})
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('welcome')  # Redirect to welcome page
    return render(request, 'accounts/register.html')
