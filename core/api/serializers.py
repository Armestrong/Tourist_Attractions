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
    address = AddressSerializer(read_only=True)
    # comments = CommentSerializer(many=True)
    # reviews = ReviewSerializers(many=True)
    complete_description = SerializerMethodField()

    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description', 'complete_description',
                  'approved',
                  'minimal_age', 'attractions',
                  'address', 'image']
        read_only_fields = ['comments', 'reviews']

    def get_complete_description(self, obj):
        return '%s - %s' % (obj.name, obj.description)

    # Method to create the attractions
    def create_attractions(self, attractions, tourist):
        for attraction in attractions:
            at = attraction.objects.create(**attraction)
            tourist.attractions.add(at)

    # override the create method to create the tourist attraction without a attracrions nested
    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']
        tourist = TouristAttraction.objects.create(**validated_data)
        self.create_attractions(attractions, tourist)

        return tourist
