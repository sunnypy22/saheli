from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.

class admin_user(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser',]


admin.site.unregister(User)
admin.site.register(User, admin_user)
