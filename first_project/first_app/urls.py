from django.contrib import admin
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('register/', views.registration, name = 'register'),
    path('login/', views.user_login, name = 'user_login'),
]
