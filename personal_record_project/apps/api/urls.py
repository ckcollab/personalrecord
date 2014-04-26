from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import workout


urlpatterns = patterns(
    '',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Index
    url(r'^$', TemplateView.as_view(template_name="api/index.html"), name="index"),

    # Workout list, GET/POST
    url(
        r'^workout/$',
        workout.WorkoutListView.as_view(),
        name='workout_list'
    ),

    # Workout detail, GET/PUT
    url(
        r'^workout/(?P<pk>[0-9]+)/$',
        workout.WorkoutDetailView.as_view(),
        name='workout_detail'
    ),

    # Set list, GET
    url(
        r'^set/$',
        workout.SetListView.as_view(),
        name='set_list'
    ),

    # Set detail, GET
    url(
        r'^set/(?P<pk>[0-9]+)/$',
        workout.SetDetailView.as_view(),
        name='set_detail'
    ),
)

