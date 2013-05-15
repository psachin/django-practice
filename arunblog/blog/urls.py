from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    """RSS feed
    """
    title = "MySite"
    description = "Some rambling of mine"
    link = "/blog/feed/"
    
    def __init__(self, ):
        """
        """
        
    def items(self):
        """list items
        
        Arguments:
        - `self`:
        """
        return Post.objects.all().order_by("-created")[:5]

    def item_title(self, item):
        """list title
        
        Arguments:
        - `self`:
        - `item`:
        """
        return item.title

    def item_description(self, item):
        """show description
        
        Arguments:
        - `self`:
        - `item`:
        """
        return item.body
    
    def item_link(self, item):
        """show link
        
        Arguments:
        - `self`:
        - `item`:
        """
        return u"/blog/%d" % (item.id)


urlpatterns = patterns('blog.views',
                       url(r'^$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created")[:5],
            template_name="blog.html")),

                       url(r'^(?P<pk>\d+)$', DetailView.as_view(
            model=Post,
            template_name="post.html")),

                       url(r'^archives/$', ListView.as_view(
            queryset=Post.objects.all().order_by("-created"),
            template_name="archives.html")),
                       url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
                       url(r'^feed/$', BlogFeed()),
                       )
