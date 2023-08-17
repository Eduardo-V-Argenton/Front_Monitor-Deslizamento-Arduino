from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    return render(request, 'configuration/index.html')

@login_required(redirect_field_name='login')
def lora_config(request):
    return render(request, 'configuration/lora_config.html')

@login_required(redirect_field_name='login')
def sys_config(request):
    return render(request, 'configuration/sys_config.html')
