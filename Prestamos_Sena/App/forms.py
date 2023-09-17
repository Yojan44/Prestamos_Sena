from django import forms
from .models import Prestamo

class PrestamosForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = '__all__'
