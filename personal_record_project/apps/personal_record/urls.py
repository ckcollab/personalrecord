from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns(
    '',
    url(r'^', include('home.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),
    )
