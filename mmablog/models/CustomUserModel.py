from django.db import models 
import uuid 
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  profile_picture = models.ImageField(upload_to="author_profile_picture/", null=True, blank=True)

  
  