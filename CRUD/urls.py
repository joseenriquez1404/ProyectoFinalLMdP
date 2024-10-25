from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.updateMenu, name="updateMenu"),
    path("update/team/show_teams/", views.showTeam, name="showTeam"),
    path("update/player/show_teams/show_players/", views.showTeamPlayers, name="showTeamPlayers"),
    path("update/player/show_teams/show_players/<int:equipo_id>/", views.teamPlayers, name="teamPlayers"),
    path("update/player/show_teams/show_players/edit_player/<int:jugador_id>/", views.editPlayer, name="editPlayer"),
    path("update/team/show_teams/<int:equipo_id>/", views.editTeam, name="editTeam"),
]