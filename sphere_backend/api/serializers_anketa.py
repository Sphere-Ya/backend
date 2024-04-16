""" Anketa serializers """
from rest_framework import serializers
from events.models import Anketa, EventSpecialization, Interest
from .serializers_interest import InterestSerializer
from .serializers_event_specialization import EventSpecializationSerializer


class AnketaSerializer(serializers.ModelSerializer):
    """ Сериализатор для отображения Анкеты интересов и специализаций """
    event_specializations = EventSpecializationSerializer(
        read_only=True,
        many=True
    )
    interests = InterestSerializer(read_only=True, many=True)

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
    """ Сериализатор для редактирования Анкеты интересов и специализаций """
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

    def to_representation(self, instance):
        return AnketaSerializer(instance, context=self.context).data
