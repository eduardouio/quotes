from rest_framework.generics import UpdateAPIView
from forwarder.models import Forwarder, Qoutation
from django.contrib.auth.models import User
from .serializers import (
    ForwarderSerializer, QoutationSerializer, UserSerializer
)


# /api/forwarder/update/
class ForwarderUpdateView(UpdateAPIView):
    serializer_class = ForwarderSerializer
    queryset = Forwarder.objects.all()


# /api/qoutation/update/
class QoutationUpdateView(UpdateAPIView):
    serializer_class = QoutationSerializer
    queryset = Qoutation.objects.all()


# /api/user/update/
class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
