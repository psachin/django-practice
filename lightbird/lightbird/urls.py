from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lightbird.views.home', name='home'),
    # url(r'^lightbird/', include('lightbird.foo.urls')),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r"^/$", 'lightbird.forum.views.main'),
                       url(r"^forum/(\d+)/$", "forum"),
                       url(r"^thread/(\d+)/$", "thread"),
)
