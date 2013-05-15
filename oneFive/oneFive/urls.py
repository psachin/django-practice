from django.conf.urls import patterns, include, url
from management.views import sign_up, register, index
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples
                       url(r'^$', index),
                       # url(r'^oneFive/', include('oneFive.foo.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'register/$', register),
                       url(r'signup/$', sign_up),
                       
                       )
