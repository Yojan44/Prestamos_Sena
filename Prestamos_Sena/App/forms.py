from django import forms
from .models import Prestamo, Devolucion

class PrestamosForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = '__all__'

class DevolucionesForm(forms.ModelForm):

    class Meta:
        model = Devolucion
        # fields = '__all__'
        fields = ['equipo_devuelto_id', 'accesorio_devuelto_id', 'fecha_devolucion']
