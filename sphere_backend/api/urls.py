from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_users import ExtensionUserViewSet
from .views_events import EventViewSet
from .views_anketa import AnketaViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', ExtensionUserViewSet)
router_v1.register('events', EventViewSet, basename='events')
router_v1.register('anketa', AnketaViewSet, basename='anketa')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # эндпоинты, для авторизации по токенам с помощью authtoken:
    path('auth/', include('djoser.urls.authtoken')),
]
