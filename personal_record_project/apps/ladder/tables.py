from django.contrib.auth import get_user_model
import django_tables2 as tables

from workout.models import Workout, Set


class SetTable(tables.Table):
    bodyweight = tables.Column(verbose_name="bodyweight", accessor="bodyweight")

    class Meta:
        model = Set
        exclude = ('id', 'video_youtube_url', 'video_local_file_name', 'tags', 'workout')
        sequence = ('bodyweight', 'exercise', 'reps', 'weight', 'notes')
