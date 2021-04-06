from dataclasses import fields

from rest_framework.serializers import ModelSerializer
from comment.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'date_post']
