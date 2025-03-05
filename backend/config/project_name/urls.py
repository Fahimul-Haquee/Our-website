# accounts/urls.py

from django.urls import path
from .views import home, register_user, login_user

urlpatterns = [
    path('', home, name='home'),        # হোম পেজ
    path('register/', register_user, name='register'),  # রেজিস্ট্রেশন পেজ
    path('login/', login_user, name='login'),  # লগইন পেজ
]
