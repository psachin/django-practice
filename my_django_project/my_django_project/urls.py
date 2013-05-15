from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_django_project.views.home', name='home'),
#    url(r'^my_django_project/', include('my_django_project.foo.urls')),
    url(r'^books/$', 'testapp.views.view_latest_books'),
    url(r'^pubs/$', 'testapp.views.view_publishers'),                       
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
)
