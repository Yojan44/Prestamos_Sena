from django.shortcuts import render

# Create your views here.
def index(request):

    # 1- Pasar datos desde View al template
    return render(request, 'html/index.html', {
        'title' : 'Inicio'
    })

def prestamos(request):

    return render(request, 'html/prestamos.html', {
        'title' : 'Prestamos'
    })

def devoluciones(request):

    return render(request, 'html/devoluciones.html')