from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('home.urls')),
    url(r'^', include('ladder.urls')),

    url(r'^api/', include('api.urls', namespace="api")),

    # Auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),
    )
