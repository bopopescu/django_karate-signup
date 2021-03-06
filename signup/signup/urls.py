"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
  #  path('', views.homepage, name='home'),
    path('', views.selecting, name='selecting'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
    path('signup', views.sign_up, name='sign_up'),
    path('new_game/', views.new_game, name='new_game'),
    path('signup_complete/', views.signup_complete, name='signup_complete'),
]
