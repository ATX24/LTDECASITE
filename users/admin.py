from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import User
from .resources import UserResource

class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource

admin.site.register(User, CustomUserAdmin)
