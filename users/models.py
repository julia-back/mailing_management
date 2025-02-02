from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField()
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        permissions = [("can_block_user", "Can block user")]
