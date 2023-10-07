from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from sensors.models import SensorsRead
from configuration.models import SensorModule

@login_required(redirect_field_name='login')
def info(request, sensor_module_id):
    # Pegar os 5 últimos
    values = SensorsRead.objects.all().filter(sensor_module=sensor_module_id).order_by('timestamp').reverse()[:5]
    last_values = []
    if values :
        last_values = SensorsRead.objects.filter(sensor_module=sensor_module_id).order_by('timestamp').last()
    return render(request, 'home/info.html', {'values': values, 'last_values': last_values})

@login_required(redirect_field_name='login')
def index(request):
    sensor_modules = SensorModule.objects.all()
    return render(request, 'home/index.html', {'sensor_modules':sensor_modules}) 