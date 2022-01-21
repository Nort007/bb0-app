from django.test import TestCase
import requests


def get_req():
    return requests.get('http://127.0.0.1:8000/sortedDataList/')


get_req()
# Create your tests here.