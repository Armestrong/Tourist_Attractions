from django.db import models
from attractions.models import ComplementAttraction


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    minimal_age = models.IntegerField()
    attractions = models.ManyToManyField(ComplementAttraction)

    def __str__(self):
        return self.name
