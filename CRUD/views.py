from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Equipo, Jugador
from .forms import EquipoForm, JugadorForm

# Create your views here.
def index(request):
    return render(request, "CRUD/index.html")

def updateMenu(request):
    return render(request, "CRUD/update_menu.html")

def showTeam(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/show_teams.html", {"equipos": equipos})

def showTeamPlayers(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/show_team_players.html", {"equipos": equipos})

def editTeam(request, equipo_id):
    equipo  = get_object_or_404(Equipo, id=equipo_id)

    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect("showTeam")
    else:
        form = EquipoForm(instance=equipo)
    
    return render(request, "CRUD/edit_team.html", {"form": form})

def teamPlayers(request, equipo_id):
    equipo  = get_object_or_404(Equipo, id=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, "CRUD/show_players.html", {"jugadores": jugadores})


def editPlayer(request,  jugador_id):
    jugador  = get_object_or_404(Jugador, id=jugador_id)
    

    if request.method == "POST":
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect("index") 
    else:
        form = JugadorForm(instance=jugador)
    
    return render(request, "CRUD/edit_player.html", {"form": form})

