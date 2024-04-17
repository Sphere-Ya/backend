"""Views api."""

from rest_framework import viewsets, generics

from events.models import (EventSpecialization, Interest)
from .serializers_event_specializations import EventSpecializationSerializer
from .serializers_interests import InterestSerializer


class InterestView(viewsets.ReadOnlyModelViewSet):
    "View для справочника направлений работы. Только GET."
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    pagination_class = None


class EventSpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для EventSpecialization.
    Работает только с GET.
    Добавить фильтрацию по interests
    """
    queryset = EventSpecialization.objects.all()
    serializer_class = EventSpecializationSerializer
    pagination_class = None
