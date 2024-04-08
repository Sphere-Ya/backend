from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'created_at',
    )
    search_fields = ('username',)
    list_filter = ('email', 'username')
    empty_value_display = '-пусто-'
