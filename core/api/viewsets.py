from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response

from core.models import TouristAttraction
from .serializers import TouristAttractionSerializer


# ViewSets define the view behavior.
class TouristAttractionViewSet(viewsets.ModelViewSet):
    serializer_class = TouristAttractionSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    search_fields = ['name', 'description', 'address__line1']

    lookup_field = "id"  # by default it's id, because id it's unique

    # --- Ways to do/filter a query

    # first
    # Simple query
    # queryset = TouristAttraction.objects.all()

    # Second
    # Filtering the query
    # def get_queryset(self):
    #     return TouristAttraction.objects.filter(approved=True)

    # Third
    # Filtering the query with query_string
    def get_queryset(self):
        queryset = TouristAttraction.objects.filter()
        pk = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if pk:
            queryset = TouristAttraction.objects.filter(pk=pk)
        if name:
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.filter(description__iexact=description)

        return queryset

    # --- Overwrite CRUD method

    # overwrite GET-list or GETAll method
    def list(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).list(request, *args, **kwargs)

    # overwrite CREATE(post) method
    def create(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).create(request, *args, **kwargs)

    # overwrite DELETE method
    def destroy(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).destroy(request, *args, **kwargs)

    # overwrite RETRIEVE(to make LOGS) method
    def retrieve(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).retrieve(request, *args, **kwargs)

    # overwrite UPDATE method
    def update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).update(request, *args, **kwargs)

    # overwrite PATH method
    def partial_update(self, request, *args, **kwargs):
        return super(TouristAttractionViewSet, self).partial_update(request, *args, **kwargs)

    # @action(methods=['post', 'get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
    #
    # @action(methods=['post', 'get'], detail=False)  # Do not need pass the res
    # def teste(self, request, pk=None):
    #     pass

    # This is a solutions to nested exist values in database with the TouristAttraction
    @action(methods=['post', 'get'], detail=True)  # Do not need pass the res
    def linking_attraction(self, request, id):
        attractions = request.data['ids']

        spots = TouristAttraction.objects.get(id=id)
        spots.attractions.set(attractions)
        spots.save()
        return HttpResponse('Attractions nested with TouristAttractions')
