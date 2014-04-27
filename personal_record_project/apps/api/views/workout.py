from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response

from personal_record_project.apps.workout.models import Workout, Set

from api.permissions import IsOwnerOrReadOnly
from api.serializers.workout import WorkoutSerializer, SetSerializer
from api.filters.workout import BodyweightFilter


class WorkoutListView(generics.CreateAPIView, generics.ListAPIView, generics.GenericAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class WorkoutDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    '''
    GET, PUT or DELETE a workout.

    You must be the owner of the workout.

    '''
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        obj = get_object_or_404(Workout, **kwargs)
        self.check_object_permissions(request, obj)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = get_object_or_404(Workout, **kwargs)
        self.check_object_permissions(request, obj)
        return self.destroy(request, *args, **kwargs)


class SetListView(generics.ListAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, BodyweightFilter)
    filter_fields = ('exercise', 'reps', 'weight')
    search_fields = ('name', 'notes')
    ordering_fields = ('reps', 'weight')


class SetDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
