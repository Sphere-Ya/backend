from datetime import timezone

from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import Event
from .serializers_events import (EventListSerializer, EventRetrieveSerializer,
                                 ParticipantSerializer, SpeakerSerializer)

User = get_user_model()


class EventViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    """Класс для вывода списка событий,
        просмотра отдельного события """
    queryset = Event.objects.filter(
        Q(level=0) &
        Q(started_at__isnull=False)
    )
    permission_classes = (permissions.AllowAny,)
    serializer_class = EventRetrieveSerializer
    # http_method_names = ['get',]

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventRetrieveSerializer


    @action(
        methods=['post'],
        detail=True,
        permission_classes=[permissions.IsAuthenticated]
    )
    def participant(self, request, pk=None):
        """"Обработчик для регистрации на событие
        залогиненного пользователя."""
        data = request.data
        data['user'] = self.request.user
        data['event'] = self.get_object()
        data['status'] = 'new'
        serializer = ParticipantSerializer(
            data=data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    @action(
        methods=['post'],
        detail=True,
        permission_classes=[permissions.IsAuthenticated]
    )
    def speaker(self, request, pk=None):
        """"Обработчик для запроса на участие в событии
        в качестве спикера залогиненного пользователя."""
        data = request.data
        user_obj = self.request.user
        if not user_obj.participant.filter(event=pk).exists():
            return Response(
                {'errors': 'You are not subscribe on this event!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        data['participant'] = user_obj.participant.get(event=pk)
        data['event'] = self.get_object()
        data['status'] = 'new'
        serializer = SpeakerSerializer(
            data=data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
