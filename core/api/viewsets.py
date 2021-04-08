from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import TouristAttraction
from .serializers import TouristAttractionSerializer


# ViewSets define the view behavior.
class TouristAttractionViewSet(viewsets.ModelViewSet):
    # queryset = TouristAttraction.objects.all()
    serializer_class = TouristAttractionSerializer

    # Filtering the query
    def get_queryset(self):
        return TouristAttraction.objects.filter(approved=True)

    # overwrite CRUD method

    # overwrite GET-list or GETAll method
    def list(self,request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).list(request, *args, **kwargs)

    # overwrite CREATE(post) method
    def create(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).create(request, *args, **kwargs)

    # overwrite DELETE method
    def destroy(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).destroy(request, *args, **kwargs)

    # overwrite RETRIVE(to make LOGS) method
    def retrieve(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).retrieve(request, *args, **kwargs)

    # overwrite UPDATE method
    def update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).update(request, *args, **kwargs)

    # overwrite PATH method
    def partial_update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['post', 'get'], detail=False)  # Do not need pass the res
    def teste(self, request, pk=None):
        pass
