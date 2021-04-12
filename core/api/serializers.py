from rest_framework.fields import SerializerMethodField
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
    complete_description = SerializerMethodField()

    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description', 'complete_description', 'complete_description2', 'approved',
                  'minimal_age', 'attractions',
                  'comments', 'reviews',
                  'address', 'image']

    def get_complete_description(self, obj):
        return '%s - %s' % (obj.name, obj.description)
