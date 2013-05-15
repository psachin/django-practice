from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """
    A blog belonging to user.

    >>> b = Blog()
    >>> b.name = 'Foo Blog'
    >>> b.user = User.objects.create(username='foo', password='test')
    >>> b.save()
    >>> print b
    Foo Blog
    
    """
    user = models.ForeignKey(User, related_name='blogs')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


