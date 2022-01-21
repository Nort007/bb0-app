from django.db.models import Aggregate
from . import serializers
from django.contrib.auth.models import User
from .models import AggregateDataModel
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class AggregateList(ListAPIView):
    queryset = AggregateDataModel.objects.all()
    serializer_class = serializers.AggregateDataSerializer

    # def get_queryset(self, *args, **kwargs):


class AddAggregateData(CreateAPIView):
    queryset = AggregateDataModel.objects.all()
    serializer_class = serializers.AggregateDataSerializer

    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)
        return Response(
            {
                'status': 200,
                'message': 'Success',
                'data': resp.data
            }
        )


class AggregateDetail(RetrieveUpdateDestroyAPIView):
    queryset = AggregateDataModel.objects.all()
    serializer_class = serializers.AggregateDataSerializer
