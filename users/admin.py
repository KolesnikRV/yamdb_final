from django.contrib import admin

from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username',
        'bio', 'email', 'role', 'user_code'
    )


admin.site.register(UserProfile, UserProfileAdmin)
