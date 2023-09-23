from django.shortcuts import render, redirect
import datetime
from App.models import Prestamo,Equipo,Accesorio
from django.core.paginator import Paginator
from django.db.models import Q

def devoluciones(request):
    prestamos = Prestamo.objects.all().order_by('-fecha_prestamo')
    # q = request.GET.get('q')
    # if q:
    #     prestamos = Prestamo.objects.filter(equipo_id__icontains=q)
    # else:
    #     prestamos = Prestamo.objects.all()
    paginator = Paginator(prestamos, 5)
    page_number = request.GET.get('page')
    prestamos = paginator.get_page(page_number)
    print(prestamos)
    return render(request, 'html/devoluciones.html', {'prestamos' : prestamos})

def devolver_equipo(request, prestamo_id):
    prestamo = Prestamo()
    prestamo = Prestamo.objects.get(prestamo_id=prestamo_id)
    prestamo.fecha_prestamo = datetime.datetime.now()
    prestamo.fecha_devolucion = datetime.datetime.now()
    prestamo.estado_prestamo = "Devuelto"
    if(prestamo.equipo_id != None):
        eqp = str(prestamo.equipo_id).split(' - ', 1)[0]
        equipo = Equipo.objects.get(numero_serie=eqp)
        print(equipo)
        equipo.estado = 'Disponible'
        equipo.save()
    if(prestamo.accesorio_id != None):
        acc = str(prestamo.accesorio_id).split(' - ', 1)[0]
        accesorio = Accesorio.objects.get(numero_serie=acc)
        accesorio.estado = 'Disponible'
        accesorio.save()
    print(prestamo)
    prestamo.save()
    return redirect('/devoluciones/')    
