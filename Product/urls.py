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
    path('shop/', views.shop, name="shop"),
    path('product_description/<int:pid>', views.product_description, name="product_description"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('del_wishlist/<int:pid>', views.del_wishlist, name="del_wishlist"),
    path('cart/', views.cart, name="cart"),
    path('cat_filter/<int:pid>', views.cat_filter, name="cat_filter"),
    path('update_cart/<int:pid>', views.update_cart, name="update_cart"),
    path('del_cart/<int:pid>', views.del_cart, name="del_cart"),
    path('checkout/', views.checkout, name="checkout"),

]
