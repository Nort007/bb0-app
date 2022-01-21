from rest_framework import serializers
from .models import SortedDataModel


class PreciseDataSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()

    class Meta:
        model = SortedDataModel
        fields = ['day', 'user_id', 'weight']
