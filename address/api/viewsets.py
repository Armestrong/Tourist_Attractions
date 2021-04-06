from rest_framework import viewsets
from address.models import Addres
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Addres.objects.all()
    serializer_class = AddressSerializer
