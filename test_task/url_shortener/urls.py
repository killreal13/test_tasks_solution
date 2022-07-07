from django.contrib import admin
from django.urls import path, include
from .views import SignUp, shortener

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='signup'),
    path('shortener/', shortener)
]