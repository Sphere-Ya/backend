""" EventSpecialization serializers """
from rest_framework import serializers
from events.models import EventSpecialization


class EventSpecializationSerializer(serializers.ModelSerializer):

    class Meta():
        model = EventSpecialization
        fields = ('id', 'name',)

