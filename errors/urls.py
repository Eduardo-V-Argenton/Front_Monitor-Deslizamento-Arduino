from django.urls import path
from . import views

urlpatterns = [
    path('<int:sensor_module_id>', views.list, name='errors'),
    path('<int:sensor_module_id>/delete/<int:error_id>/', views.delete_error, name='delete_error'),
]
