from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=False, help_text="Designates whether this user should be treated as"
                                                             " active. Unselect this instead of deleting accounts.")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta(AbstractUser.Meta):
        permissions = [("can_block_user", "Can block user")]
