from django.shortcuts import render, redirect
from App.models import Equipo, Accesorio, Inventario
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

cliente_choices = (
    ('local','Local'),
    ('regional','Regional'),
    ('otro','Otro'),
)

def inventario(request):
    equipos = Equipo.objects.all()
    #Paginador Equipos
    paginatorEquipos = Paginator(equipos, 5)
    page_number = request.GET.get('pageEquipos')
    equipos = paginatorEquipos.get_page(page_number)

    accesorios = Accesorio.objects.all()
    #Paginador Accesorios
    paginatorAccesorios = Paginator(accesorios, 5)
    page_number_acc = request.GET.get('pageAccesorios')
    accesorios = paginatorAccesorios.get_page(page_number_acc)
    return render(request, 'html/inventario.html', {'equipos' : equipos, 'accesorios' : accesorios})


@method_decorator(csrf_exempt)
def guardar_inventario(request):
    categoria = request.POST.get('categoria')

    if(request.POST.get('categoria') == 'Equipo'):
        equipo = Equipo()
        equipo.nombre = request.POST.get('nombre')
        equipo.numero_serie = request.POST.get('numero_serie')
        equipo.categoria = request.POST.get('categoria')
        print(equipo)
        equipo.save()
    else:
        accesorio = Accesorio()
        accesorio.nombre = request.POST.get('nombre')
        accesorio.numero_serie = request.POST.get('numero_serie')
        accesorio.categoria = request.POST.get('categoria')
        print(accesorio)
        accesorio.save()
    
    return redirect('/inventario/')