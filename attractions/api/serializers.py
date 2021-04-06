from rest_framework import serializers
from attractions.models import ComplementAttraction


class ComplementAttractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComplementAttraction
        fields = ['id', 'name', 'description', 'opening_hours']
