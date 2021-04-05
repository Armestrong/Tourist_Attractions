from django.db import models


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
