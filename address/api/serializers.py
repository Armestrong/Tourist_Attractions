from rest_framework.serializers import ModelSerializer
from address.models import Addres


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Addres
        fields = ['id', 'line1', 'line2', 'city', 'state', 'country', 'latitude', 'longitude']
