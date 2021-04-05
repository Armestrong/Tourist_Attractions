from rest_framework import serializers
from core.models import TouristAttraction


# Serializers define the API representation.
class TouristAttractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description']
