from django.contrib import admin

from daterange_filter.filter import DateRangeFilter

from git.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_image'] + [f.name for f in User._meta.fields]
    search_fields = ['login']
    list_filter = [('created', DateRangeFilter)]
