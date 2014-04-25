from django.conf.urls import patterns, include, url

from .views import workout


urlpatterns = patterns(
    '',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

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
)

