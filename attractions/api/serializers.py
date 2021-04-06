from rest_framework.serializers import ModelSerializer
from attractions.models import ComplementAttraction


class ComplementAttractionSerializer(ModelSerializer):
    class Meta:
        model = ComplementAttraction
        fields = ['id', 'name', 'description', 'opening_hours']
