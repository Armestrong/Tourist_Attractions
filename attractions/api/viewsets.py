from rest_framework import viewsets
from attractions.models import ComplementAttraction
from .serializers import ComplementAttractionSerializer


class ComplementAttractionViewSet(viewsets.ModelViewSet):
    queryset = ComplementAttraction.objects.all()
    serializer_class = ComplementAttractionSerializer

    filter_fields = ['name', 'description', 'opening_hours']

    # or

    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_fields = ['name', 'description', 'opening_hours']
    # obs: but you'll need delete the REST_FRAMEWORK from settings.py
