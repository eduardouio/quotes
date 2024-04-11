from rest_framework.generics import DestroyAPIView
from forwarder.models import Qoutation
from .serializers import QoutationSerializer


# /api/qoutation/delete/
class QoutationDeleteView(DestroyAPIView):
    serializer_class = QoutationSerializer
    queryset = Qoutation.objects.all()
