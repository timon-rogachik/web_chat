from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, blank=True)
    avatar = models.ImageField(upload_to='images/user/avatars', null=True, blank=True)

