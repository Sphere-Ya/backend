from rest_framework.views import permissions, status, APIView
from serializers_anketa import AnketaSerializer
from serializers_event_specialization import EventSpecializationSerializers
from serializers_interest import InterestSerializers
from serializers_users import SpecialUserSerializer
from events.models import Anketa, Interest, EventSpecialization
from users.models import User


class AnketaViewSet(APIView):
    """ Отображение анкеты пользователя """
    def get(self, request):
        user = User.objects.get(user_id=request.user_id)
        
"""
    def post(self, request):
        ...

    def put(self, request):
        ...

    def patch(self, request):
        ...
"""