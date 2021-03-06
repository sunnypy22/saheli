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
from django.contrib.auth import views as djangoview
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', djangoview.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout/', djangoview.LogoutView.as_view(), name='logout'),
    # Reset Password
    path('password-change/', djangoview.PasswordChangeView.as_view(template_name='change_password.html'),
         name='password_change'),
    path('password_change/done/',
         djangoview.PasswordChangeDoneView.as_view(template_name='password_changed_done.html'),
         name='password_change_done'),
    # Forgot Password
    path('password-reset/',
         djangoview.PasswordResetView.as_view(template_name='password_reset.html',
                                              subject_template_name='password_reset_subject.txt',
                                              email_template_name='password_reset_email.html'),
         name='password_reset'),
    path('password-reset/done/',
         djangoview.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done', ),
    path('password-reset-confirm/<uidb64>/<token>/',
         djangoview.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         djangoview.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
