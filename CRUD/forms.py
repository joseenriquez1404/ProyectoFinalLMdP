from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre_equipo", "pais_origen", "estado_origen"]