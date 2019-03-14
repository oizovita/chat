from django.contrib import admin
from .models import NameChat
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserColor


class UserColorInline(admin.StackedInline):
    model = UserColor
    can_delete = False
    verbose_name_plural = 'color'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserColorInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(NameChat)