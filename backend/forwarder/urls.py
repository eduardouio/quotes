from django.urls import path
from forwarder.api.RetrieveViews import (
    ForwarderRetrieveView,
    QoutationRetrieveView,
    UserRetrieveView
)
from forwarder.api.CreateAPIViews import (
    ForwarderCreateView,
    QoutationCreateView,
    UserCreateView
)
from forwarder.api.UpdateAPIView import (
    ForwarderUpdateView,
    QoutationUpdateView,
    UserUpdateView
)

from forwarder.api.DeleteAPIViews import QoutationDeleteView

app_name = 'qoutes'

urlpatterns = [
    path('forwarder/<int:pk>/', ForwarderRetrieveView.as_view(), name='forwarder'),
    path('forwarder/create/', ForwarderCreateView.as_view(),
         name='forwarder-create'),
    path('forwarder/update/', ForwarderUpdateView.as_view(),
         name='forwarder-update'),
    path('qoutation/<int:pk>/', QoutationRetrieveView.as_view(), name='qoutation'),
    path('qoutation/create/', QoutationCreateView.as_view(),
         name='qoutation-create'),
    path('qoutation/update/', QoutationUpdateView.as_view()),
    path('qoutation/delete/<int:pk>/', QoutationDeleteView.as_view(),
         name='qoutation-delete'),
    path('user/<int:pk>/', UserRetrieveView.as_view(), name='user'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/update/', UserUpdateView.as_view(), name='user-update'),
]
