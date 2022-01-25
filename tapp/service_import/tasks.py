import requests
from celery import shared_task
from service_api.models import AggregateDataModel
from .models import SortedDataModel


@shared_task()
def add_sorted_data_through_api():
    req = requests.get('http://web:8000/aggregateDataList/')
    for i in req.json():
        if (float(i['weight']) % 2) != 0:
            b = SortedDataModel(day=i['day'], weight=float(i['weight']))
            b.save()
    return True


@shared_task()
def sorted_data():
    obj = AggregateDataModel.objects.all()
    for i in obj:
        if (float(i.weight) % 2) != 0:
            b = SortedDataModel(day=i.day, weight=i.weight)
            b.save()
    return True


def orig_sorted_data():
    obj = AggregateDataModel.objects.all()
    for i in obj:
        if (float(i.weight) % 2) != 0:
            b = SortedDataModel(day=i.day, weight=i.weight)
            b.save()
    return True
