from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers_users import SpecialUserSerializer

User = get_user_model()


class ExtensionUserViewSet(UserViewSet):
    """Класс для вывода списка пользователей,
    просмотра и редактирования отдельного пользователя """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = SpecialUserSerializer
