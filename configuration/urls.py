from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='modules'),
    path('modules_list/', views.modules_list, name='modules_list'),
    path('<int:module_id>/', views.card, name='module_card'),
    path('<int:module_id>/lora/', views.lora_config, name='lora_config'),
    path('new/<str:module_type>/', views.new_module, name='new_module'),
    #path('<int:module_id>/delete/', views.delete_module, name='delete_module'),
    #path('<int:module_id>/edit/', views.edit_module, name='edit_module'),
]
