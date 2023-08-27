from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ControlModuleForm,SensorModule, ControlModule, SensorModuleForm, ModuleObserver
from django.contrib import messages
from django.http import Http404

@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'configuration/index.html')

@login_required(redirect_field_name='login')
def sensor_modules_list(request):
    sensor_modules = SensorModule.objects.all()
    return render(request, 'configuration/list.html', {'modules':sensor_modules})

@login_required(redirect_field_name='login')
def new_module(request, module_type):
    if module_type == "controller" and not ControlModule.objects.exists():
        form = ControlModuleForm(request.POST if request.method == 'POST' else None)
    elif module_type == "sensor":
        form = SensorModuleForm(request.POST if request.method == 'POST' else None)
    else:
        raise Http404("Tipo inválido")
    if request.method == 'POST':
        if form.is_valid():
            module = form.save()
            messages.success(request, 'Criação bem sucedida')
            observer = ModuleObserver(is_controller=(True if module_type=="controller" else False), module=module)
            observer.save()
            return redirect('sensors_list' if module_type =='sensor' else 'index')
    return render(request, 'configuration/form.html', {'form':form})

@login_required(redirect_field_name='login')
def edit_sensor_module(request, module_id):
    sensor_module = get_object_or_404(SensorModule, id=module_id)
    form = SensorModuleForm(request.POST if request.method == 'POST' else None,instance=sensor_module)
    if request.method == 'POST':
        if form.is_valid():
            module = form.save()
            messages.success(request, 'Edição bem sucedida')
            observer = ModuleObserver(is_controller=False, module=module)
            observer.save()
            return redirect('sensors_list')
    return render(request, 'configuration/form.html', {'form':form})

@login_required(redirect_field_name='login')
def edit_control_module(request):
    control_module = ControlModule.objects.first()
    form = ControlModuleForm(request.POST if request.method == 'POST' else None, instance=control_module)
    if request.method == 'POST':
        if form.is_valid():
            module = form.save()
            messages.success(request, 'Edição bem sucedida')
            observer = ModuleObserver(is_controller=True, module=module)
            observer.save()
            return redirect('index')
    return render(request, 'configuration/form.html', {'form':form})

@login_required(redirect_field_name='login')
def delete_sensor_module(request, module_id):
    sensor_module = get_object_or_404(SensorModule, id=module_id)
    sensor_module.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('sensors_list')
