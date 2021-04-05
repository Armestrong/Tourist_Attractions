from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_post = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
