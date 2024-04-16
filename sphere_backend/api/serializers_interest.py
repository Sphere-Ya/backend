""" Interest serializers """
from rest_framework import serializers
from events.models import Interest
from .serializers_event_specialization import EventSpecializationSerializers


class InterestSerializers(serializers.ModelSerializer):

    class Meta():
        model = Interest
        fields = ('id', 'name',)
        # 'event_specializations'

