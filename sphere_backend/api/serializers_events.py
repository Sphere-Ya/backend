"""Event serializers."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from events.models import (
    Event, EventSpecialization, Speaker,
    )
from .serializers_address import (
    BuildingSerializer, StreetSerializer,
    CitySerializer, CountrySerializer
)

User = get_user_model()


class SpeakerSerializer(serializers.ModelSerializer):
    """Cериализатор для спикера"""

    class Meta:
        fields = '__all__'
        model = Speaker


class EventSpecializationSerializer(serializers.ModelSerializer):
    """Cериализатор для специализаций"""

    class Meta:
        fields = ['id', 'name',]
        model = EventSpecialization


class EventListSerializer(serializers.ModelSerializer):
    """Cериализатор для списка событий (list)"""
    city = serializers.SerializerMethodField()
    event_specializations = EventSpecializationSerializer(many=True, read_only=True)
    started_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    ended_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        fields = ['id', 'name', 'description', 'started_at', 'ended_at',
                  'is_online', 'link', 'is_offline', 'address_comment', 'city',
                  'event_specializations']
        model = Event

    def get_city(self, obj):
        city = ""
        if obj.building is not None:
            city = obj.building.street.city.name
        return city


class EventRetrieveSerializer(EventListSerializer):
    """Cериализатор для события (retrieve)"""
    children = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    # speaker = serializers.SpeakerSerializer(read_only=True)

    class Meta:
        fields = ['id', 'name', 'description', 'started_at', 'ended_at',
                  'is_online', 'link', 'is_offline', 'address_comment',
                  'address', 'event_specializations', 'children',]
        # 'speaker',
        model = Event

    def get_children(self, obj):
        if obj.children is not None:
            return EventRetrieveSerializer(obj.children, many=True).data
        return None

    def get_address(self, obj):
        data = {}
        if obj.building is not None:
            data['country'] = CountrySerializer(
                obj.building.street.city.country).data
            data['city'] = CitySerializer(
                obj.building.street.city).data
            data['street'] = StreetSerializer(
                obj.building.street).data
            data['building'] = BuildingSerializer(
                obj.building).data
        return data
