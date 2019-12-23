from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.upload import avatar_path
from utils.validators import image_size, image_extension


class MainUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to=avatar_path, validators=[image_size, image_extension], default='default'
                                                                                                       '/avatar.jpg',
                              null=True)
    bio = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
