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
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from Home import views as index_view

admin.site.site_header = "Saheli administration"
admin.site.site_title = "Saheli administration"
admin.site.index_title = "Welcome To Saheli administration"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view.index, name="index"),
    path('home/', include('Home.urls')),
    path('account/', include('Account.urls')),
    path('product/', include('Product.urls')),
    path('order/', include('Order.urls')),
]

urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT,
}),
                ]
