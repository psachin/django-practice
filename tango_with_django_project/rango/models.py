from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # this line is req. links userprofile to a user model instance
    user = models.OneToOneField(User)
    
    # additional attrebutes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    
    # unicode stuf
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
        
        
