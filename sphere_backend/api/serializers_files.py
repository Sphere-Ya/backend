""" File serializers """
from rest_framework import serializers
from events.models import File


class FileSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='type_of_file'
    )

    class Meta():
        model = File
        fields = ('id', 'name', 'link', 'type')
