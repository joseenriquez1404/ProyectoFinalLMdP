from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.updateMenu, name="updateMenu"),
    path("update/show_teams/", views.showTeam, name="showTeam"),
    path("update/show_teams/show_players/", views.showTeamPlayers, name="showTeamPlayers"),
    path("update/show_teams/show_players/<int:equipo_id>/", views.teamPlayers, name="teamPlayers"),
    path("update/show_teams/<int:equipo_id>/", views.editTeam, name="editTeam"),
]