""" Anketa serializers """
from rest_framework import serializers
from events.models import Anketa, EventSpecialization, Interest
from .serializers_interest import InterestSerializers
from .serializers_event_specialization import EventSpecializationSerializers


class AnketaSerializer(serializers.ModelSerializer):
    event_specializations = EventSpecializationSerializers(
        read_only=True,
        many=True
    )
    interests = InterestSerializers(read_only=True, many=True)

    class Meta():
        model = Anketa
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'job_position',
            'job_title',
            'experience',
            'event_specializations',
            'interests'
        ]


class AnketaSerializerAdd(serializers.ModelSerializer):
    event_specializations = serializers.PrimaryKeyRelatedField(
        queryset=EventSpecialization.objects.all(),
        many=True,
        required=True,
        allow_empty=False
    )
    interests = serializers.PrimaryKeyRelatedField(
        queryset=Interest.objects.all(),
        many=True,
        required=True,
        allow_empty=False
    )

    class Meta():
        model = Anketa
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'job_position',
            'job_title',
            'experience',
            'event_specializations',
            'interests'
        ]