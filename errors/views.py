from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Errors


@login_required(redirect_field_name='login')
def list(request, sensor_module_id):
    errors = Errors.objects.all().filter(sensor_module=sensor_module_id)
    return render(request, 'errors/list.html', {'errors':errors, 'sensor_module_id':sensor_module_id})

@login_required(redirect_field_name='login')
def delete_error(request,sensor_module_id, error_id):
    error = get_object_or_404(Errors, id=error_id)
    error.delete()
    return redirect('errors', sensor_module_id)
