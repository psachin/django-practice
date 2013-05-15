from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ["name"]

        '''
        This ordering = ["name"] bit tells Django that unless an
        ordering is given explicitly with order_by(), all publishers
        should be ordered by name.
        '''

    class Admin:
        pass

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='./headshot')

    def __unicode__(self):
        return "%s %s" %(self.first_name, self.last_name)

    class Admin:
        pass

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

    class Admin:
        pass



