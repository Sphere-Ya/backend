from rest_framework import mixins, viewsets
from rest_framework.permissions import SAFE_METHODS
from .serializers_anketa import AnketaSerializer, AnketaSerializerAdd
from events.models import Anketa
from .permissions import OwnerFullAccess


class AnketaViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """ Отображение анкеты пользователя """
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = (OwnerFullAccess,)

    def get_serializer_class(self):
        """ Выбираем какой сериализатор использовать """
        if self.request.method in SAFE_METHODS:
            return AnketaSerializer  # Для отображения
        return AnketaSerializerAdd  # Для добавления и редакирования

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
