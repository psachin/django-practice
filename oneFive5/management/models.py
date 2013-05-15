from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sr_no = models.IntegerField()

    def __unicode__(self):  
        return self.user  
    
#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['sr_no']



 
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
 
post_save.connect(create_user_profile, sender=User)
 
User.profile = property(lambda u: u.get_profile())


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
        
# post_save.connect(create_user_profile, sender=User)
    

    

