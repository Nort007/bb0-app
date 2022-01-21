from django.db import models
from datetime import datetime
# Create your models here.


class SortedDataModel(models.Model):
    day: datetime = models.DateTimeField()
    user_id: int = models.AutoField(primary_key=True)
    weight: float = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ['day', 'weight']
