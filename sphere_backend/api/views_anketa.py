from rest_framework import mixins, permissions, viewsets
from serializers_anketa import AnketaSerializer
from serializers_event_specialization import EventSpecializationSerializers
from serializers_interest import InterestSerializers
from serializers_users import SpecialUserSerializer
from events.models import Anketa, Interest, EventSpecialization
from users.models import User


class AnketaViewSet(
    mixins.CreatModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """ Отображение анкеты пользователя """
    queryset = Anketa.objects.all()
    serializer_class = AnketaSerializer
    permission_classes = (permissions.IsAuthenticated,)
