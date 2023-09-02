from django.shortcuts import render,redirect
from configuration.models import ModuleObserver
from django.contrib import messages
from os import environ 
from django.views.decorators.csrf import csrf_exempt

def get_data(request):
    pass

def send_command(request):
    observer = ModuleObserver.objects.filter(executed=False).order_by("-timestamp").first()
    message = ' '
    if(observer):
        message = observer.print_command()
    return render(request, 'communication/command.html', {'message':message})

@csrf_exempt
def get_response(request):
    key = "6dc8a0fb"
    if request.method != 'POST':
        return redirect('commands')
    if request.POST.get('key') == key:
        response = request.POST.get('response')
        observer = ModuleObserver.objects.filter(executed=False).order_by("-timestamp").first()
        if observer:
            if response == '1':
                observer.executed = True
                observer.save()
            elif response == '-1':
                messages.error(request, 'Ocorreu um erro')
    return redirect('index')

