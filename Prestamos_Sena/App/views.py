from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            # Verifica que el usuario sea un superusuario
            login(request, user)
            
            # Cambia 'pagina_principal' por la URL a la que deseas redirigir al usuario después del login
            return redirect('prestamos/')  

    return render(request, 'html/acceso.html')


# def devoluciones(request):

#     return render(request, 'html/devoluciones.html')

def inicio(request):
    
    return render(request, 'html/inicio.html')