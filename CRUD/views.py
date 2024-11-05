from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Equipo, Jugador
from .forms import EquipoForm, JugadorForm

# Index


def index(request):
    return render(request, "CRUD/index.html")

# Update Functions


def updateMenu(request):
    return render(request, "CRUD/Update/update_menu.html")


def showTeam(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Update/show_teams.html", {"equipos": equipos})


def showTeamPlayers(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Update/show_team_players.html", {"equipos": equipos})


def editTeam(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)

    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect("showTeam")
    else:
        form = EquipoForm(instance=equipo)

    return render(request, "CRUD/Update/edit_team.html", {"form": form})


def teamPlayers(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, "CRUD/Update/show_players.html", {"jugadores": jugadores})


def editPlayer(request,  jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)

    if request.method == "POST":
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = JugadorForm(instance=jugador)

    return render(request, "CRUD/Update/edit_player.html", {"form": form})

# Swow Functions


def showMenu(request):
    return render(request, "CRUD/Show/show_menu.html")


def showTeams(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Show/show_teams.html", {"equipos": equipos})


def teams(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Show/show_team.html", {"equipos": equipos})


def teamPlayer(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, "CRUD/Show/show_players.html", {"jugadores": jugadores})

# CREATE FUNCIONS


def createMenu(request):
    return render(request, "CRUD/Create/create_menu.html")


def createTeam(request):
    if request.method == "POST":
        equipos = EquipoForm(request.POST)
        if equipos.is_valid():
            equipos.save()
            return redirect("index")
    else:
        equipos = EquipoForm()
    return render(request, "CRUD/create/create_teams.html", {"equipos": equipos})


def createPlayer(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        jugadores = JugadorForm(request.POST)
        if jugadores.is_valid():
            jugador = jugadores.save(commit=False)
            jugador.equipo = equipo
            jugador.save()
            return redirect('index')
    else:
        jugadores = JugadorForm()

    return render(request, "CRUD/create/create_players.html", {"jugadores": jugadores})


def createShowPlayers(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Create/create_show_players.html", {"equipos": equipos})


# Delete functions

def deleteMenu(request):
    return render(request, "CRUD/Delete/delete_menu.html")


def deleteShowTeams(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Delete/delete_show_teams.html", {"equipos": equipos})


def deleteTeamAction(request, equipo_id):
    equipos = Equipo.objects.filter(id=equipo_id)
    equipos.delete()
    return render(request, "CRUD/Delete/delete_team_action.html")


def deleteShowTeamPlayer(request):
    equipos = Equipo.objects.all()
    return render(request, "CRUD/Delete/delete_show_team_player.html", {"equipos": equipos})


def deletePlayer(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    jugador = Jugador.objects.filter(equipo=equipo)
    return render(request, "CRUD/Delete/delete_show_players_to_delete.html", {"jugadores": jugador})


def deletePlayerAction(request, jugador_id):
    jugador = Jugador.objects.filter(id=jugador_id)
    jugador.delete()
    return render(request, "CRUD/Delete/delete_player_action.html")
