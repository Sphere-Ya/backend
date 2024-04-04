"""User serializers."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SpecialUserSerializer(serializers.ModelSerializer):
    """Cериализатор для пользователей"""
    is_participant = serializers.SerializerMethodField()

    class Meta:
        fields = ['id', 'email', 'username', 'is_participant']
        model = User

    def get_is_participant(self, obj):
        """Получаем список всех подписок пользователя на конференции"""
        # request = self.context.get('request', None)
        # if request.user.is_authenticated:
        #     return obj.participant.filter(user=request.user).exists()
        return False
