from django.contrib.auth import get_user_model
import django_tables2 as tables

from workout.models import Workout, Set


class SetTable(tables.Table):


    class Meta:
        model = Set
        exclude = ('id', 'video_youtube_url', 'video_local_file_name', 'tags', 'workout')
        sequence = ('exercise', 'reps', 'weight', 'notes')
        attrs = {"class": "paleblue"}
