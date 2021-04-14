from django.db import models
from attractions.models import ComplementAttraction
from comment.models import Comment
from review.models import Review
from address.models import Addres
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class IdentifierDoc(models.Model):
    description = models.CharField(max_length=100)


class TouristAttraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    minimal_age = models.IntegerField(null=True, blank=True)
    attractions = models.ManyToManyField(ComplementAttraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Addres, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='tourist_attractions', null=True, blank=True)
    identifier_doc = models.OneToOneField(IdentifierDoc, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    # @property
    # def complete_description2(self):
    #     return '%s - %s' % (self.name, self.description)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        return token.key
