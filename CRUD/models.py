from django.db import models


class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    estado_origen = models.CharField(max_length=100)


class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre_jugador = models.CharField(max_length=200)
    apellido_jugador = models.CharField(max_length=200)
    numero_playera = models.IntegerField()
    fecha_nacimiento = models.DateField("fecha nacimieto")
    posicion_campo = models.CharField(max_length=100)
