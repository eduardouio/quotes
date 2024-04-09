from rest_framework.generics import RetrieveAPIView
from .models import Forwarder, Qoutation
from django.contrib.auth.models import User
from .serializers import (
    ForwarderSerializer, QoutationSerializer, UserSerializer
)


# /api/forwarder/<pk>/
class ForwarderRetrieveView(RetrieveAPIView):
    serializer_class = ForwarderSerializer
    queryset = Forwarder.objects.all()


# /api/qoutation/<pk>/
class QoutationRetrieveView(RetrieveAPIView):
    serializer_class = QoutationSerializer
    queryset = Qoutation.objects.all()

# /api/user/<pk>/


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
