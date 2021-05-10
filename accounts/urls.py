from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = "main" # defince This is main App

urlpatterns = [
    path("register/", views.register, name="user-register"),
    path("login", views.login_request, name="login"),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),  # logout_request, name ="logout"),
    path("profile", views.profile, name="user-profile"),
]
