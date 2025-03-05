from django.urls import path
from .views import home, register_user, login_user

urlpatterns = [
    path("", home, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
]
from django.urls import path
from .views import home, register_user, login_user, welcome_page

urlpatterns = [
    path("", home, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("welcome/", welcome_page, name="welcome"),  # ওয়েলকাম পেজের URL
]
