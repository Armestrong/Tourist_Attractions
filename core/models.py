from django.db import models
from attractions.models import ComplementAttraction
from comment.models import Comment
from review.models import Review
from address.models import Addres


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    minimal_age = models.IntegerField()
    attractions = models.ManyToManyField(ComplementAttraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Addres, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
