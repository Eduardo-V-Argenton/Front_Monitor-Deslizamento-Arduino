from django.db import models
from configuration.models import SensorModule

# Create your models here.
class Errors(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)   
    message=models.TextField(blank=False, null=False)
    sensor_module = models.ForeignKey(to=SensorModule, on_delete=models.DO_NOTHING)
