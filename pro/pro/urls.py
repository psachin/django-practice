from django.conf.urls import patterns, include, url
from books.views import manage_authors, show_authors
from polls.views import contact


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pro.views.home', name='home'),
    # url(r'^pro/', include('pro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', contact),
                       #    url(r'^add/$', add_publisher),
    url(r'^authors/$', manage_authors),                       
                       #    url(r'^author/$', manage_author),                       
    url(r'^show/$', show_authors),
)
