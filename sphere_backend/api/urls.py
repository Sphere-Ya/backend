from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_users import ExtensionUserViewSet
from .views_events import EventViewSet
from .views import (EventSpecializationViewSet, InterestView)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', ExtensionUserViewSet)
router_v1.register('events', EventViewSet, basename='events')
router_v1.register('event-specialization', EventSpecializationViewSet)
router_v1.register('interest', InterestView)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # эндпоинты, для авторизации по токенам с помощью authtoken:
    path('auth/', include('djoser.urls.authtoken')),
]
