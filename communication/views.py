from django.shortcuts import render
from configuration.models import SensorModule, ControlModule, ModuleObserver


def get_data(request):
    pass

def send_command(request):
    observer = ModuleObserver.objects.last()
    message = ' '
    if(observer):
        message = observer.print_command()
    return render(request, 'communication/command.html', {'message':message})
