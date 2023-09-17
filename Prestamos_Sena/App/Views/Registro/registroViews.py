from django.shortcuts import render, redirect
from App.models import Aprendiz
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def registro(request):

    # 1- Pasar datos desde View al template
    return render(request, 'html/registro.html', {
        'title' : 'Inicio'
    })

@method_decorator(csrf_exempt)
def registrar(request):
    aprendiz = Aprendiz()
    aprendiz.aprendiz_id = request.POST.get('aprendiz_id')
    aprendiz.nombre = request.POST.get('nombre')
    aprendiz.correo = request.POST.get('correo')
    aprendiz.tipo_documento = request.POST.get('tipo_documento')
    aprendiz.numero_documento = request.POST.get('numero_documento')
    aprendiz.ficha_aprendiz = request.POST.get('ficha_aprendiz')
    aprendiz.save()
    print(request.POST)
    return redirect('/registro/')

