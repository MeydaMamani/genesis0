from django.contrib import admin
# from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *
app_name="dashboard"

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]