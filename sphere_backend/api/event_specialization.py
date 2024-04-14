""" EventSpecialization serializers """
from django.contrib.auth import get_user_model
from rest_framework import serializers
from events.models import EventSpecialization


class EventSpecializationSerializers(serializers.ModelSerialazer):

    class Meta():
        model = EventSpecialization
        fields = ('id', 'name')