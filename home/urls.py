from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sensor_module_id>', views.info, name='info'),
    path('<int:sensor_module_id>/calibrate', views.calibrate, name='calibrate'),
]
