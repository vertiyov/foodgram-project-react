from django.shortcuts import render
from rest_framework import mixins, viewsets
from users.models import User
from .serializers import UserSerializer, UserCreateSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return UserSerializer
        return UserCreateSerializer
