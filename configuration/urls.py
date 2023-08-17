from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='configurations'),
    path('lora/', views.lora_config, name='lora_config'),
    path('sys/', views.sys_config, name='sys_config'),
]
