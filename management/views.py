# En views.py de tu aplicación o proyecto
from django.shortcuts import render

""" def home(request):
    return render(request, 'home/home.html') """

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

def loguear(request):
    error = None
    if request.method == 'POST':
        user = request.POST ['user']
        password = request.POST ['password']
        auth_user = authenticate(username = user, password = password)
        if auth_user is not None:
            login(request, auth_user)
            return render(request, 'home.html')
        else:
             error = 'Usuario o contraseña incorrectos'
             return render(request, 'login.html', {'error':error})
    return render(request, 'login.html')