"""Saheli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('product/blog/', views.blog, name="blog"),
    path('product/blog_detail/', views.blog_detail, name="blog_detail"),
    path('product/about/', views.about, name="about"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('product/faqs/', views.faqs, name="faqs"),
    path('demo/', views.demo, name="demo"),
    path('filter_data/', views.filter_data, name="filter_data"),
    path('try_ajax/', views.try_ajax, name="try_ajax"),

]
