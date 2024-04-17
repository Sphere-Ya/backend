"""Views api."""

from rest_framework import viewsets, generics
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import filters, status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from events.models import (EventSpecialization, Interest)
from .serializers_event_specializations import EventSpecializationSerializer
from .serializers_interests import InterestSerializer


class InterestView(viewsets.ReadOnlyModelViewSet):
    "View для справочника направлений работы. Только GET."
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class EventSpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для EventSpecialization.
    Работает только с GET.
    Добавить фильтрацию по interests
    """
    queryset = EventSpecialization.objects.all()
    serializer_class = EventSpecializationSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('interest',)
