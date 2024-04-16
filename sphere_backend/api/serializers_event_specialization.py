""" EventSpecialization serializers """
from rest_framework import serializers
from events.models import EventSpecialization


class EventSpecializationSerializers(serializers.ModelSerializer):

    class Meta():
        model = EventSpecialization
        fields = ('id', 'name')
