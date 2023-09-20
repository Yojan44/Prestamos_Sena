from django import forms
from .models import Prestamo, Devolucion

class PrestamosForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrestamosForm, self).__init__(*args, **kwargs)

        # Personaliza el campo fecha_prestamo
        self.fields['fecha_prestamo'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})

class DevolucionesForm(forms.ModelForm):

    class Meta:
        model = Devolucion
        # fields = '__all__'
        fields = ['equipo_devuelto_id', 'accesorio_devuelto_id', 'fecha_devolucion']
