from django.core.exceptions import ObjectDoesNotExist

from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from personal_record_project.apps.workout.models import Workout

from api.serializers.workout import WorkoutSerializer


class WorkoutListView(generics.CreateAPIView, generics.ListAPIView, generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs);
