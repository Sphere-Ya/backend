from rest_framework import mixins, permissions, viewsets
from .serializers_anketa import AnketaSerializer
from .serializers_event_specialization import EventSpecializationSerializers
from .serializers_interest import InterestSerializers
from .serializers_users import SpecialUserSerializer
from events.models import Anketa, Interest, EventSpecialization
from users.models import User
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

    def perform_create(self, serializer):
        anketa = Anketa.objects.filter(user=self.request.user).exists
        print(anketa)
        if (anketa):
            return
        else:
            serializer.save(user=self.request.user)
