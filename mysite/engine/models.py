from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    "Profile for a user"
    user = models.OneToOneField(User)
    

