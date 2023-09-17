from django.shortcuts import render

# Create your views here.
def index(request):

    # 1- Pasar datos desde View al template
    return render(request, 'html/acceso.html', {
        'title' : 'Inicio'
    })


def devoluciones(request):

    return render(request, 'html/devoluciones.html')