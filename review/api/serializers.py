from rest_framework.serializers import ModelSerializer
from review.models import Review


class ReviewSerializers(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rate', 'post_date']
