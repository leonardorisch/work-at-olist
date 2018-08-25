from django.db import models
from calls.models import *

class BillCall(models.Model):
    call = models.OneToOneField(
        EndCall,
        on_delete=models.CASCADE
    )
    destination = models.CharField(max_length=15)
    start_date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    price = models.FloatField()

class Bill(models.Model):
    subscriber = models.CharField(max_length=15)
    period = models.DurationField()
    calls = models.ManyToManyField(BillCall)
