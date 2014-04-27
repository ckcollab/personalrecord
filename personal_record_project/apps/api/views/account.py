from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework import permissions
from rest_framework import generics

from api.permissions import IsOwnerOrReadOnly
from api.serializers.account import AccountSerializer
from personal_record_project.apps.user_profile.models import UserProfile


class AccountDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        obj = get_object_or_404(UserProfile, **kwargs)
        self.check_object_permissions(request, obj)
        return self.update(request, *args, **kwargs)
