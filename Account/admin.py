from django.contrib import admin
from django.contrib.auth.models import User, Group


# Register your models here.

class admin_user(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser',]
    list_filter = ['username', 'email',]
    readonly_fields = ['email','username','first_name','last_name','password','last_login','date_joined']


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, admin_user)
