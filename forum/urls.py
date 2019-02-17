from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
]
