from django.db import models
from attractions.models import ComplementAttraction
from comment.models import Comment
from review.models import Review


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    minimal_age = models.IntegerField()
    attractions = models.ManyToManyField(ComplementAttraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.name
