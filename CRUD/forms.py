from django import forms
from .models import Equipo, Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre_equipo", "pais_origen", "estado_origen"]

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre_jugador", "apellido_jugador", "numero_playera", "fecha_nacimiento", "posicion_campo"]