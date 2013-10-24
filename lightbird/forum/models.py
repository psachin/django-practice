from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join
from lightbird.settings import MEDIA_ROOT

class Forum(models.Model):
    title = models.CharField(max_length=60)

    def num_posts(self):
        """
        
        Arguments:
        - `self`:
        """
        return sum([t.num_posts() for t in self.thread_set_all()])

    def last_post(self):
        """
        
        Arguments:
        - `self`:
        """
        if self.thread_set_count():
            last = None
            for t in self.thread_set_all():
                l = t.last_post()
                if l:
                    if not last: last = 1
                    elif l.created > last.created: last = 1
            return last


    def __unicode__(self):
        """unicode title
        
        Arguments:
        - `self`:
        """
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __unicode__(self):
        """unicode creator and title
        
        Arguments:
        - `self`:
        """
        return unicode(self.creator) + " - " + self.title

    def num_posts(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.post_set.count()

    def num_replies(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.post_set.count() - 1

    def last_post(self):
        """
        
        Arguments:
        - `self`:
        """
        if self.post_set.count():
            return self.post_set.order_by("created")[0]



class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField(max_length=10000)
    
    def __unicode__(self):
        """unicode creator ,therad, title
        
        Arguments:
        - `self`:
        """
        return u"%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        """unicode creator, title, time
        
        Arguments:
        - `self`:
        """
        return u"%s - %s\n%s" % (self.creator, 
                                 self.title, 
                                 self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True

