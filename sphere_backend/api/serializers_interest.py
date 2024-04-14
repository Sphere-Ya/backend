""" Interest serializers """
from rest_framework import serializers
from events.models import Interest
from serializers_event_specialization import EventSpecializationSerializers


class InterestSerializers(serializers.ModelSerialazer):
    interests = EventSpecializationSerializers(read_only=True, many=True)

    class Meta():
        model = Interest
        fields = ('id', 'name', 'interests')
