from django.conf.urls import patterns, include, url
from clock.views import current_datetime, hours_ahead, sample_template, load_image
from books.views import contact

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       
                       
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       # 
                       url(r'^time/$', current_datetime),
                       url(r'^time/plus/(\d+)/$', hours_ahead),                       
                       url(r'sample/$', sample_template),                   
                       url(r'contact/$', contact),                   
                       url(r'image/$', load_image),                   
                       url(r'^login/$', 'django.contrib.auth.login'),
     
)
