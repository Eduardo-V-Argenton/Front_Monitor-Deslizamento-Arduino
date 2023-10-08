from django.shortcuts import render,redirect, get_object_or_404
from configuration.models import ModuleObserver, SensorModule
from sensors.models import SensorsRead
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import time, timedelta
from django.utils import timezone
from configuration.models import SensorModule
from .getWebWeatherInfo import get_web_weather_info  

key = "6dc8a0fb"

@csrf_exempt
def get_data(request):
    if request.method != 'POST':
        return redirect('commands')
    if request.POST.get('key') == key:
        data = request.POST.get('data')
        sensors_read = data.split(';')

        # ToDo ataulizar valor de periculosidade

        sensor_module = get_object_or_404(SensorModule,id=sensors_read[5]);
        weather_info = get_web_weather_info(sensor_module.city, sensor_module.country)
        soil_moisture = (int(sensors_read[3]) - sensor_module.air_soil_moisture_value) * 100 / (sensor_module.water_soil_moisture_value - sensor_module.air_soil_moisture_value) 
        instance = SensorsRead(
            accel_x=float(sensors_read[0]) if sensors_read[0] != 'nan' else 0.0,
            accel_y=float(sensors_read[1]) if sensors_read[1] != 'nan' else 0.0,
            accel_z=float(sensors_read[2]) if sensors_read[2] != 'nan' else 0.0,
            soil_moisture=soil_moisture if soil_moisture != 'nan' else 0,
            rain_sensor_value=int(sensors_read[4]) if sensors_read[4] != 'nan' else 0,
            sensor_module=sensor_module,
            air_temperature= float(weather_info[1]),
            air_humidity= float(weather_info[0])
        )
        instance.save()
    return redirect('index')

def send_command(request):
    observer = ModuleObserver.objects.filter(executed=False).order_by("-date").first()
    message = ' '
    if(observer):
        message = observer.print_command()
    else:
        all_sensors = SensorModule.objects.all()
        for sensor in all_sensors:
            if sensor.next_sensors_read <= timezone.now():
                message=sensor.print_sensors_read_command()
                seconds_delta = timedelta(seconds=sensor.auto_send_sensors_period)
                sensor.next_sensors_read = timezone.now() + seconds_delta
                sensor.save()
                break
    return render(request, 'communication/command.html', {'message':message})

@csrf_exempt
def get_response(request):
    if request.method != 'POST':
        return redirect('commands')
    if request.POST.get('key') == key:
        response = request.POST.get('response')
        observer = ModuleObserver.objects.filter(executed=False).order_by("-date").first()
        if observer:
            if int(response) > 0:
                observer.executed = True
                observer.save()
            elif int(response) <= 0:
                messages.error(request, 'Ocorreu um erro')
    return redirect('index')

