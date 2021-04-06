from rest_framework import viewsets
from core.models import TouristAttraction
from .serializers import TouristAttractionSerializer


# ViewSets define the view behavior.
class TouristAttractionViewSet(viewsets.ModelViewSet):
    queryset = TouristAttraction.objects.all()
    serializer_class = TouristAttractionSerializer
