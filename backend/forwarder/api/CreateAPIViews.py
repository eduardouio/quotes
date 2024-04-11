from rest_framework.generics import CreateAPIView
from forwarder.models import Forwarder, Qoutation
from django.contrib.auth.models import User
from .serializers import (
    ForwarderSerializer, QoutationSerializer, UserSerializer
)


# /api/forwarder/create/
class ForwarderCreateView(CreateAPIView):
    serializer_class = ForwarderSerializer
    queryset = Forwarder.objects.all()


# /api/qoutation/create/
class QoutationCreateView(CreateAPIView):
    serializer_class = QoutationSerializer
    queryset = Qoutation.objects.all()


# /api/user/create/
class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
