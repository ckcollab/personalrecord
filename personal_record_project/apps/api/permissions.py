from rest_framework import permissions

from personal_record_project.apps.user_profile.models import UserProfile
from personal_record_project.apps.workout.models import Workout, Set


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # For user profile
        if type(obj) == UserProfile:
            return obj == request.user

        if type(obj) == Workout or type(obj) == Set:
            return obj.user == request.user

        raise Exception("Checking against unknown type %s, error!" % type(obj))

