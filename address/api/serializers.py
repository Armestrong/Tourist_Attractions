from rest_framework import serializers
from address.models import Addres


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addres
        fields = ['id', 'line1', 'line2', 'city', 'state', 'country', 'latitude', 'longitude']
