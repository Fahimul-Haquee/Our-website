from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# একটি সিম্পল ভিউ তৈরি (যদি home ভিউ না থাকে)
def home(request):
    return HttpResponse("Welcome to the Home Page!")

urlpatterns = [
    path("admin/", admin.site.urls),  # অ্যাডমিন প্যানেল
    path("", home),  # হোমপেজ URL
    path("api/", include("accounts.urls")),  # API রুট, accounts অ্যাপে urls.py ফাইল থাকতে হবে
]
from django.urls import path
from accounts.views import home

urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),  # এই লাইনটি আপনার প্রোজেক্টের মূল urls.py ফাইলে থাকতে হবে
]
from django.contrib import admin
from django.urls import path
from accounts.views import home, register_user, login_user, welcome_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('welcome/', welcome_page, name='welcome'),
]
