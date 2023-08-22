from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='modules'),
    path('sensors_list/', views.sensor_modules_list, name='sensors_list'),
    path('new/<str:module_type>/', views.new_module, name='new_module'),
    path('delete/<int:module_id>/', views.delete_sensor_module, name='delete_sensor'),
    path('edit/<str:module_type>/<int:module_id>/', views.edit_module, name='edit_module'),
]
