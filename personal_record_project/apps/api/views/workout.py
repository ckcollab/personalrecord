from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from personal_record_project.apps.workout.models import Workout

from api.permissions import IsOwnerOrReadOnly
from api.serializers.workout import WorkoutSerializer


class WorkoutListView(generics.CreateAPIView, generics.ListAPIView, generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class WorkoutDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print args
        print kwargs
        obj = get_object_or_404(Workout, **kwargs)
        self.check_object_permissions(request, obj)
        return self.update(request, *args, **kwargs)
