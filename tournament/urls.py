from django.urls import path
from .views import TournamentAddAPI, TournamentView, InvitationView, InvitationStatusView, UpdateTournamentView, DeleteTournament

urlpatterns = [
    path('add/', TournamentAddAPI.as_view()),
    path('retrive/<int:pk>', TournamentView.as_view()),
    path('invite/', InvitationView.as_view()),
    path('status/', InvitationStatusView.as_view()),
    path('update/<int:pk>',UpdateTournamentView.as_view()),
    path('delete/<int:pk>',DeleteTournament.as_view())

]