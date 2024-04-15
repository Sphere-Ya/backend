from datetime import timezone

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import (Event, EventSpecialization, File,
                           Interest, Participant, Speaker)
from .serializers_events import EventListSerializer, EventRetrieveSerializer

User = get_user_model()


class EventViewSet(viewsets.ModelViewSet):
    """Класс для вывода списка событий,
        просмотра отдельного события """
    queryset = Event.objects.filter(
        Q(level=0) &
        Q(started_at__isnull=False)
    )
    serializer_class = EventRetrieveSerializer
    http_method_names = ['get',]

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventRetrieveSerializer
