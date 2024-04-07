from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (EventSpecialization, Event,
                     File, Interest, Participant, Speaker)


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


class EventMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    list_display = (
        'name',
        'started_at',
        'ended_at',
    )


admin.site.register(Event, EventMPTTModelAdmin)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'event',
        'participation_format',
        'status'
    )
    search_fields = ('user', 'event')
    list_filter = ('user', 'event')
    empty_value_display = '-пусто-'


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = (
        'participant',
        'event',
        'type',
    )
    search_fields = ('participant', 'event')
    list_filter = ('participant', 'event')
    empty_value_display = '-пусто-'
