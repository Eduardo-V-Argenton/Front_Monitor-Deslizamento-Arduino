from django.urls import path
from . import views

urlpatterns = [
    path('commands/', views.send_command, name='commands'),
    path('response/', views.get_response, name='response'),
    path('data/', views.get_data, name="get_data")
]
