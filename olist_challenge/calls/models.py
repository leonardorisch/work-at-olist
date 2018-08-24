from django.db import models

class Call(models.Model):
    call_id = models.PositiveIntegerField()
    timestamp = models.CharField(max_length=50)
    class Meta:
        abstract = True

class StartCall(Call):
    origin = models.CharField(max_length=15, db_index=True)
    destination = models.CharField(max_length=15)
    type = models.CharField(max_length=5, default="start")

class EndCall(Call):
    type = models.CharField(max_length=5, default="end")
