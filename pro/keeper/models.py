# Create your models here.
from django.db import models

class Author(models.Model):   
    name = models.CharField(max_length=100)
    age = models.IntegerField()   
    friends = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return self.name

class Publisher(models.Model):   
    name = models.CharField(max_length=300)   
    num_awards = models.IntegerField()

    def __unicode__(self):
        return self.name

class Book(models.Model):   
    isbn = models.CharField(max_length=9)   
    name = models.CharField(max_length=300)   
    pages = models.IntegerField()   
    price = models.DecimalField(max_digits=10, decimal_places=2)   
    rating = models.FloatField()   
    authors = models.ManyToManyField(Author)   
    publisher = models.ForeignKey(Publisher)   
    pubdate = models.DateField()

    def __unicode__(self):
        return self.name

