""" Anketa serializers """
from django.contrib.auth import get_user_model
from rest_framework import serializers
from events.models import Anketa


class AnketaSerializer(serializers.ModelSerialazer):
    
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
            'event_anketa',
            'itnterest_anketa'
        ]
