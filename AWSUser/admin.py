from django.contrib import admin
from .models import User
from unfold.admin import ModelAdmin
from django.contrib.auth.models import Group

#unregister group
admin.site.unregister(Group)

@admin.register(User)
class AdminAWSMember(ModelAdmin):
    list_display=('email','is_superuser','is_staff','is_active')
    list_filter=('is_superuser','is_staff','is_active')

