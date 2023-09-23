from django.shortcuts import render, redirect
from django.forms import forms
from App.models import Prestamo, Devolucion, Usuario, Aprendiz, Equipo, Accesorio
from App.forms import PrestamosForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def prestamos(request):
    prestamosForm = PrestamosForm()
    return render(request, 'html/prestamos.html', {'form' : prestamosForm})


def guardar_prestamo(request):
    prestamosForm = PrestamosForm(request.POST)
    equipo_id = prestamosForm.data['equipo_id']
    accesorio_id = prestamosForm.data['accesorio_id']
    if prestamosForm.is_valid():
        if (equipo_id == '') & (accesorio_id == ''):
            messages.warning(request, 'Debe seleccionar un equipo o un accesorio primero.')
            return redirect('/prestamos/')
        else:
            print(request.POST)
            prestamosForm.save()
            return redirect('/prestamos/')
    return redirect('/prestamos/')
