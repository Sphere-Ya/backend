from django.contrib import admin

from .models import Anketa, EventSpecialization, File, Interest


@admin.register(EventSpecialization)
class EventSpecializationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Anketa)
class AnketaAdmin(admin.ModelAdmin):

    list_display = (
        'users',
        'first_name',
        'last_name',
        'email',
        'phone',
        'job_position',
        'job_title',
        'experience',
        'interests',
        'event_specializations',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    list_filter = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    empty_value_display = '-пусто-'
