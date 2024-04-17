"""Event serializers."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from events.models import (Anketa, Event, Participant, Speaker,)
from .serializers_addresses import (BuildingSerializer, StreetSerializer,
                                    CitySerializer, CountrySerializer)
from .serializers_event_specializations import EventSpecializationSerializer
from .serializers_files import FileSerializer

User = get_user_model()


class SpeakerforEventSerializer(serializers.ModelSerializer):
    """Cериализатор для спикера"""

    personal_data = serializers.SerializerMethodField()

    class Meta:
        fields = ['id', 'type', 'personal_data']
        model = Speaker

    def get_personal_data(self, obj):
        """Необходимо отдавать данные из анкеты
        имя, фамилию, место работы, должность
        Спикером может быть только зарегистрированный на событие пользователь,
        поэтому проверку на наличие анкеты не делаем
        Фото прикрепляется через модель File с типом avatar"""

        user = obj.participant.user
        anketa = Anketa.objects.get(user=user)
        data = {}
        data['first_name'] = anketa.first_name
        data['last_name'] = anketa.last_name
        data['job_position'] = anketa.job_position
        data['job_title'] = anketa.job_title
        return data


class AddressSerializer(serializers.Field):
    """Cериализатор для адреса"""

    def to_representation(self, value) -> dict[str, dict] | None:
        data = {
            'country': {},
            'city': {},
            'street': {},
            'building': {}
        }
        if value is not None:
            data['country'] = CountrySerializer(
                value.street.city.country).data
            data['city'] = CitySerializer(
                value.street.city).data
            data['street'] = StreetSerializer(
                value.street).data
            data['building'] = BuildingSerializer(
                value).data
        return data


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
    address = AddressSerializer(source='building')
    files = FileSerializer(many=True, read_only=True)
    speakers = SpeakerforEventSerializer(many=True, read_only=True)

    class Meta:
        fields = ['id', 'name', 'description', 'started_at', 'ended_at',
                  'is_online', 'link', 'is_offline', 'address_comment',
                  'address', 'event_specializations', 'files', 'speakers',
                  'children',]
        # 'speaker',
        model = Event

    def get_children(self, obj) -> list | None:
        if obj.children is not None:
            return EventRetrieveSerializer(obj.children, many=True).data
        return None


class ParticipantSerializer(serializers.ModelSerializer):
    """Cериализатор для специализаций"""

    event = EventRetrieveSerializer(
        read_only=True,
    )

    class Meta:
        fields = ['event', 'participation_format', 'status']
        model = Participant

    def validate(self, data):
        request = self.context.get('request', None)
        data = self.initial_data
        if request.method == 'POST':
            if data['event'].participant.filter(user=data['user']).exists():
                raise serializers.ValidationError(
                    'You are participant this event already!')
        return data


class SpeakerSerializer(serializers.ModelSerializer):
    """Cериализатор для спикера"""

    event = EventRetrieveSerializer(
        read_only=True,
    )

    class Meta:
        fields = ['event', 'type', 'status']
        model = Speaker

    def validate(self, data):
        request = self.context.get('request', None)
        data = self.initial_data
        if request.method == 'POST':
            if data['event'].speakers.filter(participant=data['participant']).exists():
                raise serializers.ValidationError(
                    'You are speaker this event already!')
        return data
