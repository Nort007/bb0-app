from .tasks import add_sorted_data_through_api, orig_sorted_data, sorted_data
from . import serializers
from django.shortcuts import render
from rest_framework import generics
from .models import SortedDataModel
from rest_framework.views import APIView
from rest_framework.response import Response


class OrigSortedTask(APIView):
    def get(self, request):
        if request.method == 'GET':
            orig_sorted_data()
        return Response(
            {
                'status': 200,
                'message': 'Сортировка без очередей с блокировкой страницы и юзера'
            }
        )


class SortedTask(APIView):
    # Run import task
    def get(self, request):
        if request.method == 'GET':
            sorted_data.apply_async()
        return Response(
            {
                'status': 200,
                'message': 'Success'
            }
        )


class SortedDataThroughApi(APIView):
    def get(self, request):
        if request.method == 'GET':
            add_sorted_data_through_api.apply_async()
        return Response(
            {
                'status': 200,
                'message': 'Сортировка нечетных чисел посредством вызова Апи из service_api'
            }
        )


class SortedDataList(APIView):
    def get(self, request):
        if request.method == 'GET':
            sorted_data = SortedDataModel.objects.all()
            serializer = serializers.PreciseDataSerializer(sorted_data, many=True)
            print(Response.status_code)
            return Response(
                {
                    "status": Response.status_code,
                    "sortedData": serializer.data[0]
                 },
            )
