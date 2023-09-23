from django.shortcuts import render, redirect
import datetime
from App.models import Prestamo
from django.core.paginator import Paginator
from django.db.models import Q

def devoluciones(request):
    prestamos = Prestamo.objects.all()
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
    print(prestamo)
    prestamo.save()
    return redirect('/devoluciones/')    
