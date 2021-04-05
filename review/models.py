from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
