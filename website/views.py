from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ingreso correcto")
            return redirect('home')
        else:
            messages.success(request, "Ingreso de usuario y/o contraseña incorrecto, intente nuevamente")
            return redirect('home')
    else:    
        return render(request, 'home.html', {})

#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Sesión cerrada")
    return redirect('home')

