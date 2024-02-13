from django.contrib import admin
from django.urls import path
from blogapp.views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
]
