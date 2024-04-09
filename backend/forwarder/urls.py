from django.urls import path
from forwarder.api.RetrieveViews import (
    ForwarderRetrieveView, QoutationRetrieveView, UserRetrieveView)

app_name = 'qoutes'

urlpatterns = [
    path('forwarder/<int:pk>/', ForwarderRetrieveView.as_view(), name='forwarder'),
    path('qoutation/<int:pk>/', QoutationRetrieveView.as_view(), name='qoutation'),
    path('user/<int:pk>/', UserRetrieveView.as_view(), name='user'),
]
