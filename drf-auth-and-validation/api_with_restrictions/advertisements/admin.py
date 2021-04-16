from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from advertisements.models import User, Advertisement


admin.site.register(Advertisement)


admin.site.register(User, UserAdmin)
