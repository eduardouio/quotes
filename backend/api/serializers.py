from forwarder.models import Forwarder, Qoutation
from django.contrib.auth.models import User
from rest_framework import serializers


class ForwarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forwarder
        fields = '__all__'


class QoutationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoutation
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password', 'groups', 'user_permissions',
            'is_staff', 'is_active', 'is_superuser', 'last_login',
            'date_joined'
        ]
