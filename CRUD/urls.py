from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.updateMenu, name="updateMenu"),
    path("update/team/show_teams/", views.showTeam, name="showTeam"),
    path("update/player/show_teams/show_players/",
         views.showTeamPlayers, name="showTeamPlayers"),
    path("update/player/show_teams/show_players/<int:equipo_id>/",
         views.teamPlayers, name="teamPlayers"),
    path("update/player/show_teams/show_players/edit_player/<int:jugador_id>/",
         views.editPlayer, name="editPlayer"),
    path("update/team/show_teams/<int:equipo_id>/",
         views.editTeam, name="editTeam"),
    path("show/", views.showMenu, name="showMenu"),
    path("show/teams/", views.showTeams, name="showTeams"),
    path("show/players/", views.teams, name="teams"),
    path("show/players/<int:equipo_id>/", views.teamPlayer, name="teamPlayer"),
    path("create/create_teams", views.createTeam, name="createTeam"),
    path("create/", views.createMenu, name="createMenu"),
    path("create/show_players/create_players/<int:equipo_id>",
         views.createPlayer, name='createPlayer'),
    path("create/show_players", views.createShowPlayers, name="createShowPlayer"),
    path("delete/delete_menu", views.deleteMenu, name='deleteMenu'),
    path("delete/delete_teams", views.deleteShowTeams, name="deleteTeams"),
    path("delete/deleted_team/<int:equipo_id>",
         views.deleteTeamAction, name="deleteTeamAction"),
    path("delete/show_team_players",
         views.deleteShowTeamPlayer, name="deleteShowTeamPlayer"),
    path("delete/players_to_delete/<int:equipo_id>",
         views.deletePlayer, name="deletePlayer"),
    path("delete/delete_player_action/<int:jugador_id>",
         views.deletePlayerAction, name='deletePlayerAction')
]
