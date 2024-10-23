from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.updateMenu, name="updateMenu"),
    path("update/show_teams/", views.showTeam, name="showTeam"),
    path("update/show_teams/<int:equipo_id>/", views.editTeam, name="editTeam"),
    path("showTeams/", views.showTeam, name="ShowTeams")
]