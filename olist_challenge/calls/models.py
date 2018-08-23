from django.db import models

class Call(models.Model):
    id = models.AutoField(primary_key=True)
    call_id = models.PositiveIntegerField(db_index=True)
    type = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=50)
    class Meta:
        abstract = True

class StartCall(Call):
    origin = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)

class EndCall(Call):
    pass
