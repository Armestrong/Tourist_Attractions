from django.db import models


class ComplementAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    image = models.ImageField(upload_to='attractions', null=True, blank=True)

    def __str__(self):
        return self.name

