from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^genres/$', 'myapp.views.show_genres'),

# Examples:
    # url(r'^$', 'test_mptt.views.home', name='home'),
    # url(r'^test_mptt/', include('test_mptt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
