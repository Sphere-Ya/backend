"""Views api."""

from rest_framework import viewsets, generics
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from events.models import (EventSpecialization, Interest)
from api.serializers import (EventSpecializationSerializer, InterestSerializer)


class InterestView(generics.ListAPIView):
    "View для справочника направлений работы. Только GET."
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class EventSpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для EventSpecialization.
    Работает только с GET.
    В декораторе @action разрешенна работа со списком объектов
    и переопределён URL на презентабельный.
    В декораторе @permission_classes разрешён доступ для незалогиненных.
    Фильтр выдаст последние пять записей с именем программист.
    """
    queryset = EventSpecialization.all()
    serializer_class = EventSpecializationSerializer

    @action(
        methods=['get'], detail=False, url_path='recent-developer-interest'
    )
    @permission_classes([AllowAny])
    def recent_developer_interest(self, request):
        try:
            interests = Interest.objects.filter(name='Программист')[:5]
            serializer = self.get_serializer(interests, many=True)

            return Response(serializer.data)

        except Interest.DoesNotExist:
            return Response(
                {"message": "No interests found for 'Программист'"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as rest:
            return Response(
                {"message": "An error occurred", "error": str(rest)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


'''
class InterestViewSet(viewsets.ModelViewSet):
    """ViewSet для Interest."""
    queryset = Interest.all()
    serializer_class = InterestSerializer


class EventSpecializationView(generics.ListAPIView):
    "View для справочника специализаций. Только GET."
    queryset = EventSpecialization.objects.all()
    serializer_class = EventSpecializationSerializer


class EventSpecializationViewSet(viewsets.ModelViewSet):
    """ViewSet для EventSpecialization."""
    queryset = EventSpecialization.all()
    serializer_class = EventSpecializationSerializer
'''
