from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    # username
    # password
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
