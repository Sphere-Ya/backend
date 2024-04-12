from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (Anketa, Event, EventSpecialization, File,
                     Interest, Participant, Speaker, Country, City, Street,
                     Building)


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
        'get_interests',
        'get_event_specializations',
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

    def get_event_specializations(self, obj):
        return "\n".join([p.name for p in obj.event_specializations.all()])

    def get_interests(self, obj):
        return "\n".join([p.name for p in obj.interests.all()])


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

@admin.register(Country)
class CountyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
