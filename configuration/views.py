from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LoraConfigForm, SensorModule, ControlModule
from django.contrib import messages

@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'configuration/index.html')

@login_required(redirect_field_name='login')
def lora_config(request):
    if request.method == 'POST':
        form = LoraConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Criação bem sucedida')
            return redirect(index)
    else:
        form = LoraConfigForm()
    return render(request, 'configuration/lora_config.html', {'form':form})
