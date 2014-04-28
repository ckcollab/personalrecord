from rest_framework import serializers

from personal_record_project.apps.workout.models import Workout, Set


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('id', 'person', 'bodyweight', 'exercise', 'weight', 'reps', 'notes', 'video_youtube_url', 'video_local_file_name', 'gender')


class WorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)

    class Meta:
        model = Workout
        fields = ('id', 'user', 'bodyweight', 'sets', 'gender')
