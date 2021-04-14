from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from attractions.models import ComplementAttraction
from address.models import Addres
from core.models import TouristAttraction, IdentifierDoc
from attractions.api.serializers import ComplementAttractionSerializer
from comment.api.serializers import CommentSerializer
from address.api.serializers import AddressSerializer
from review.api.serializers import ReviewSerializers

# Serializers define the API representation.
from review.models import Review


class IdentifierDocSerializer(ModelSerializer):
    class Meta:
        model = IdentifierDoc
        fields = '__all__'


class TouristAttractionSerializer(ModelSerializer):
    attractions = ComplementAttractionSerializer(many=True)
    address = AddressSerializer()
    # comments = CommentSerializer(many=True)
    # reviews = ReviewSerializers(many=True)
    complete_description = SerializerMethodField()
    identifier_doc = IdentifierDocSerializer()

    class Meta:
        model = TouristAttraction
        fields = ['id', 'name', 'description', 'complete_description',
                  'approved',
                  'minimal_age', 'attractions', 'address', 'comments', 'reviews', 'image', 'identifier_doc']
        read_only_fields = ['comments']

    # Method to create the attractions
    def create_attractions(self, attractions, tourist):
        for attraction in attractions:
            at = ComplementAttraction.objects.create(**attraction)
            tourist.attractions.add(at)

    # override the create method to create the tourist attraction without a attracrions nested
    # everytime that the create method is called, they will nest with the others fields
    def create(self, validated_data):
        # Taking the values and deleting from the validated_data

        # ManyToMany
        attractions = validated_data['attractions']
        del validated_data['attractions']

        # ForeignKey
        addrss = validated_data['address']
        del validated_data['address']

        # OneToOne
        doc = validated_data['identifier_doc']
        del validated_data['identifier_doc']

        #
        reviews = validated_data['review']
        del validated_data['review']

        # Creating a instance of TouristAttraction and passing validated_data that i modify
        endpoint = TouristAttraction.objects.create(**validated_data)

        # adding the values that was taking out
        self.create_attractions(attractions, endpoint)

        adrs = Addres.objects.create(**addrss)
        endpoint.address = adrs

        ind_doc = IdentifierDoc.objects.create(**doc)
        endpoint.identifier_doc = ind_doc

        endpoint.review.set(reviews)

        # saving the modifies and returning
        endpoint.save()

        return endpoint

    def get_complete_description(self, obj):
        return '%s - %s' % (obj.name, obj.description)
