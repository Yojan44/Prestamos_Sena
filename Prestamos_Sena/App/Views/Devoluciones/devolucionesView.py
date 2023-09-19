from django.shortcuts import render, redirect
from time import gmtime, strftime
import datetime
from django.forms import forms
from App.models import Prestamo, Devolucion, Usuario, Aprendiz, Equipo, Accesorio
from App.forms import DevolucionesForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def devoluciones(request):
    # devolucionesForm = DevolucionesForm()
    prestamos = Prestamo.objects.all()
    print(prestamos)
    return render(request, 'html/devoluciones.html', {'prestamos' : prestamos})


def devolver_equipo(request, prestamo_id):
    prestamo = Prestamo()
    prestamo = Prestamo.objects.get(prestamo_id=prestamo_id)
    prestamo.fecha_prestamo = datetime.datetime.now()
    prestamo.estado_prestamo = "Devuelto"
    print(prestamo)
    prestamo.save()
    # prestamo.
    return redirect('/devoluciones/')    
