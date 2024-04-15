from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_users import ExtensionUserViewSet
from .views import (EventSpecializationViewSet, InterestView)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', ExtensionUserViewSet)
router_v1.register('EventSpecialization', EventSpecializationViewSet)
router_v1.register('Interest', InterestView)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # эндпоинты, для авторизации по токенам с помощью authtoken:
    path('auth/', include('djoser.urls.authtoken')),
    path('eventSpecialization/', include(router_v1.urls)),
    path('interest/', include(router_v1.urls))
]
