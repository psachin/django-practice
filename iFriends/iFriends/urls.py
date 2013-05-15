from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from People.views import index, details, person_form
from home.views import contact_view
from summ.views import calculate, add, value, jq
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


details1 = {'opts':('name','email')}
details2 = {'opts':('name','bday')}
details3 = {'opts':('name', 'desc', 'favoriteURL')}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iFriends.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$', index),
    url(r'^people/$', details),
    url(r'^people/info/(?P<pID>\d+)/$', details), # (?P<name>pattern)
    url(r'^People/Contact/(?P<pID>\d+)/$', 'details', details1),
    url(r'^People/Birthday/(?P<pID>\d+)/$', 'details', details2),
    url(r'^People/Details/(?P<pID>\d+)/$', 'details', details3),
                       
    url(r'^contact/$', contact_view),                       
    url(r'^person/form/(?P<pID>\d+)/$',person_form),
    url(r'^calculator/$', calculate),                       
    url(r'^add/$', add),                       
    url(r'^js/$', value),                       
    url(r'^jq/$', jq),                           
)




''''
urlpatterns += patterns( '',
    url(r'^people/$', index),
    url(r'^people/$', details),
    url(r'^people/info/(?P<pID>\d+)/$', details), # (?P<name>pattern)
    url(r'^People/Contact/(?P<pID>\d+)/$', 'details', details1),
    url(r'^People/Birthday/(?P<pID>\d+)/$', 'details', details2),
    url(r'^People/Details/(?P<pID>\d+)/$', 'details', details3),

)
'''''
