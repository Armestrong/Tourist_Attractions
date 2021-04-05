from django.db import models


class ComplementAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()

    def __str__(self):
        return self.name
