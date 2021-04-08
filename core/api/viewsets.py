from rest_framework import viewsets
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


'''
    # overwrite CRUD method

    # overwrite GET-list or GETAll method
    def list(self, *args, **kwargs):
        return Response({'teste': 123})

    # overwrite CREATE(post) method
    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['name']})

    # overwrite DELETE method
    def destroy(self, request, *args, **kwargs):
        pass

    # overwrite RETRIVE(to make LOGS) method
    def retrieve(self, request, *args, **kwargs):
        pass

    # overwrite UPDATE method
    def update(self, request, *args, **kwargs):
        pass

    # overwrite PATH method
    def partial_update(self, request, *args, **kwargs):
        pass
'''
