from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AggregateDataModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AggregateDataSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = AggregateDataModel
        fields = ['day', 'user_id', 'weight', 'unit']
