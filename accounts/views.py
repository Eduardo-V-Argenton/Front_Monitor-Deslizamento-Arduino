from django.shortcuts import render,redirect
from django.contrib import messages, auth

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username);
    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('login')
