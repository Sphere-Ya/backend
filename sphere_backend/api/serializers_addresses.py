"""Address serializers."""
from rest_framework import serializers

from events.models import (Building, City, Country, Street)


class BuildingSerializer(serializers.ModelSerializer):
    """Cериализатор для дома и координат"""

    class Meta:
        fields = ['id', 'name','latitude', 'longitude']
        model = Building


class StreetSerializer(serializers.ModelSerializer):
    """Cериализатор для улицы"""

    class Meta:
        fields = ['id', 'name', ]
        model = Street


class CitySerializer(serializers.ModelSerializer):
    """Cериализатор для города"""

    class Meta:
        fields = ['id', 'name',]
        model = City


class CountrySerializer(serializers.ModelSerializer):
    """Cериализатор для страны"""

    class Meta:
        fields = ['id', 'name',]
        model = Country
