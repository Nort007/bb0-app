from django.db import models
from datetime import datetime
# Create your models here.


class AggregateDataModel(models.Model):
    day: datetime = models.DateTimeField(auto_now_add=True)
    user_id: int = models.AutoField(primary_key=True)
    weight: float = models.FloatField(null=False, blank=False)
    unit: str = models.CharField(max_length=32, null=False, default='kg')

    class Meta:
        ordering = ['day', 'weight']
