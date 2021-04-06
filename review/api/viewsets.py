from rest_framework.viewsets import ModelViewSet
from review.models import Review
from .serializers import ReviewSerializers


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
