from rest_framework.serializers import ModelSerializer
from core.models import TouristAttraction
from attractions.api.serializers import ComplementAttractionSerializer
from comment.api.serializers import CommentSerializer
from address.api.serializers import AddressSerializer
from review.api.serializers import ReviewSerializers


# Serializers define the API representation.
class TouristAttractionSerializer(ModelSerializer):
    attractions = ComplementAttractionSerializer(many=True)
    comments = CommentSerializer(many=True)
    address = AddressSerializer()
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description', 'approved', 'minimal_age', 'attractions', 'comments', 'reviews',
                  'address', 'image']
