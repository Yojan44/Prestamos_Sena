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

def registro(request):

    # 1- Pasar datos desde View al template
    return render(request, 'html/registro.html', {
        'title' : 'Inicio'
    })

def prestamos(request):

    return render(request, 'html/prestamos.html', {
        'title' : 'Prestamos'
    })

def devoluciones(request):

    return render(request, 'html/devoluciones.html')