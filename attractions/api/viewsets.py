from rest_framework import viewsets
from attractions.models import ComplementAttraction
from .serializers import ComplementAttractionSerializer


class ComplementAttractionViewSet(viewsets.ModelViewSet):
    queryset = ComplementAttraction.objects.all()
    serializer_class = ComplementAttractionSerializer
