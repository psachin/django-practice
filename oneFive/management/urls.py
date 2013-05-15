from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'management.views',
    url(r'register/$','register'),
)
