from django.urls import path
from . import views

urlpatterns = [
    path('commands/', views.send_command, name='commands'),
    path('data/', views.get_data, name="get_data")
]
