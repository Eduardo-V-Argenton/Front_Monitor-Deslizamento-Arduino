from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='modules'),
    path('sensors_list/', views.sensor_modules_list, name='sensors_list'),
    path('new/<str:module_type>/', views.new_module, name='new_module'),
    path('delete/<int:module_id>/', views.delete_sensor_module, name='delete_sensor'),
    path('edit/sensor/<int:module_id>/', views.edit_sensor_module, name='edit_sensor_module'),
    path('edit/controller/', views.edit_control_module, name='edit_control_module'),
]
