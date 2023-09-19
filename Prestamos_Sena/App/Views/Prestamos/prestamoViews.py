from django.shortcuts import render, redirect
from django.forms import forms
from App.models import Prestamo, Devolucion, Usuario, Aprendiz, Equipo, Accesorio
from App.forms import PrestamosForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def prestamos(request):
    prestamosForm = PrestamosForm()
    return render(request, 'html/prestamos.html', {'form' : prestamosForm})


def guardar_prestamo(request):
    prestamosForm = PrestamosForm(request.POST)
    if prestamosForm.is_valid():
        print(request.POST)
        prestamosForm.save()
        return redirect('/prestamos/')
    return redirect('/prestamos/')
