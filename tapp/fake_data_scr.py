from service_api.models import AggregateDataModel
from random import randint

for i in range(1, 10000):
    b = AggregateDataModel(weight=float(randint(100, 200)))
    b.save()
