from django.shortcuts import render, redirect
from django.forms import forms
from App.models import Prestamo, Devolucion, Usuario, Aprendiz, Equipo, Accesorio
from App.forms import PrestamosForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# def prestamos(request):
#     # form = PrestamosForm()
#     equipos = Equipo.objects.all()
#     accesorios = Accesorio.objects.all()
#     usuarios = Usuario.objects.all()
#     aprendices = Aprendiz.objects.all()
#     return render(request, 'html/prestamos.html',{
#         'title' : 'Prestamos',
#         "equipos" : equipos,
#         "accesorios" : accesorios,
#         "usuarios" : usuarios,
#         "aprendices" : aprendices
#     })
def prestamos(request):
    prestamosForm = PrestamosForm()
    return render(request, 'html/prestamos.html', {'form' : prestamosForm})


def guardar_prestamo(request):
    prestamosForm = PrestamosForm(request.POST)
    if prestamosForm.is_valid():
        print(request.POST)
        prestamosForm.save()
        return render(request, 'html/prestamos.html', {'form' : prestamosForm})
    return render(request, 'html/prestamos.html', {'form' : prestamosForm})
    redirect('/prestamos/')
    # selected_city_obj_list = Aprendiz.objects.filter(pk__in=city_pk_list)
    # print(selected_city_obj_list)
    # prestamo.accesorio_id = request.POST.get('accesorio')
    # prestamo.equipo_id = request.POST.get('equipo')
    # prestamo.usuario_id = request.POST.get('usuario')
    # prestamo.aprendiz_id = request.POST.get('ficha')
    # print(request.POST)