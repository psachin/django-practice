from django.db import models
from django.contrib.auth.models import User
# Create your models here.

gender_list=(
    ('M','Male'),
    ('F','Female')
    )

class Blog(models.Model):
    title = models.CharField( 'Title', max_length=200)
    text = models.TextField('Text', max_length=2048)
    
class Person(models.Model):
    userid = models.ForeignKey(User, primary_key=True)
    name = models.CharField('Name',max_length=200)
    email = models.EmailField('E-mail',unique=True)
    bday = models.DateField('Birth date', blank=True)
    gender = models.CharField('Gender',max_length=1,choices=gender_list)
    favoriteURL = models.URLField('Website',blank=True)
    headshot = models.ImageField('Photo',upload_to='headshot',blank=True)
    desc = models.TextField('Description',max_length=500,blank=True,)
    friends = models.ManyToManyField('self',blank=True)
    blogs = models.ManyToManyField(Blog,blank=True)
    
    def __str__(self):
        return '%s'%(self.name)


