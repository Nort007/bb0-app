from . import tasks
from . import serializers
from django.shortcuts import render
from rest_framework import generics
from .models import SortedDataModel
from rest_framework.views import APIView
from rest_framework.response import Response


class OrigSortedTask(APIView):
    # Run import task
    def get(self, request):
        if request.method == 'GET':
            tasks.orig_sorted()
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
            tasks.sorted_data.apply_async()
        return Response(
            {
                'status': 200,
                'message': 'Success'
            }
        )


class SortedDataThroughApi(APIView):
    def get(self, request):
        if request.method == 'GET':
            tasks.add_sorted_data_through_api.apply_async()
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
            print(sorted_data)
            serializer = serializers.PreciseDataSerializer(sorted_data, many=True)
            return Response({"sortedData": serializer.data})
