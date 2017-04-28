from django.contrib import admin

from git.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_image'] + [f.name for f in User._meta.fields]
