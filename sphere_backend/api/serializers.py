""""Serializers."""

from rest_framework import serializers

from events.models import EventSpecialization, Interest


class EventSpecializationSerializer(serializers.ModelSerializer):
    """Серилизатор справочник специализаций."""

    class Meta:
        model = EventSpecialization
        fields = ['id', 'name']


class InterestSerializer(serializers.ModelSerializer):
    """Серилизатор справочник направлений работы."""
    event_specializations = serializers.StringRelatedField(
        many=True, read_only=True
    )  # Для того, чтобы отображалось name, вместо id

    class Meta:
        model = Interest
        fields = ['id', 'name', 'event_specializations']
