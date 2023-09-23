from django.shortcuts import render, redirect
from django.forms import forms
from App.models import Prestamo, Devolucion, Usuario, Aprendiz, Equipo, Accesorio
from App.forms import PrestamosForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def prestamos(request):
    prestamosForm = PrestamosForm()
    # prestamosForm.fields['category'].queryset = Equipo.objects.filter(estado_equipo='user')
    return render(request, 'html/prestamos.html', {'form' : prestamosForm})


def guardar_prestamo(request):
    equipo = Equipo()
    accesorio = Accesorio()
    prestamosForm = PrestamosForm(request.POST)
    equipo_i = prestamosForm.data['equipo_id']
    accesorio_i = prestamosForm.data['accesorio_id']
    if prestamosForm.is_valid():
        if (equipo_i == '') & (accesorio_i == ''):
            messages.warning(request, 'Debe seleccionar un equipo o un accesorio primero.')
            return redirect('/prestamos/')
        else:
            print(request.POST)
            prestamosForm.save()
            if(equipo_i != ''):
                equipo = Equipo.objects.get(equipo_id=equipo_i)
                print(equipo)
                equipo.estado = 'Prestado'
                equipo.save()
            if(accesorio_i != ''):
                accesorio = Accesorio.objects.get(accesorio_id=accesorio_i)
                accesorio.estado = 'Prestado'
                accesorio.save()
            return redirect('/prestamos/')
    return redirect('/prestamos/')
