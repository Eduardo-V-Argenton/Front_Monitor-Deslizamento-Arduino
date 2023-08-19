from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ControlModuleForm, LoraConfig, LoraConfigForm, Module, SensorModule, ControlModule, SensorModuleForm
from django.contrib import messages
from django.http import Http404
from .extras.security_functions import gen_hash

@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'configuration/index.html')

@login_required(redirect_field_name='login')
def lora_config(request, module_id):
    if request.method == 'POST':
        form = LoraConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Criação bem sucedida')
            return redirect(index)
    else:
        lora_config = LoraConfig.objects.get(module=module_id)
        if not lora_config:
            form = LoraConfigForm()
        else:
            form = LoraConfigForm(lora_config)
    return render(request, 'configuration/lora_config.html', {'form':form})

@login_required(redirect_field_name='login')
def card(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    return render(request, 'configuration/card.html', {'module':module})

@login_required(redirect_field_name='login')
def modules_list(request):
    sensor_modules = SensorModule.objects.all()
    return render(request, 'configuration/list.html', {'sensor_modules':sensor_modules})

@login_required(redirect_field_name='login')
def new_module(request, module_type):
    if module_type == "controller":
        form = ControlModuleForm(request.POST if request.method == 'POST' else None)
    elif module_type == "sensor":
        form = SensorModuleForm(request.POST if request.method == 'POST' else None)
    else:
        raise Http404("Tipo inválido")
    if request.method == 'POST':
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.hash = gen_hash()
            form_instance.save()
            messages.success(request, 'Criação bem sucedida')
            return redirect(index)
    return render(request, 'configuration/form.html', {'form':form})
