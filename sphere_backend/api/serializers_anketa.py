""" Anketa serializers """
from django.contrib.auth import get_user_model
from rest_framework import serializers
from events.models import Anketa
from serializers_interest import InterestSerializers
from serializers_event_specialization import EventSpecializationSerializers


class AnketaSerializer(serializers.ModelSerialazer):
    event_specializations = EventSpecializationSerializers(
        read_only=True,
        many=True
    )
    interests = InterestSerializers(read_only=True, many=True)

    class Meta():
        model = Anketa
        fields = [
            'id',
            'user_anketa',
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
