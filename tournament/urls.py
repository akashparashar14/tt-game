from django.urls import path
from .views import TournamentAddAPI, TournamentView, InvitationView

urlpatterns = [
    path('add/', TournamentAddAPI.as_view()),
    path('retrive/<int:pk>', TournamentView.as_view()),
    path('invite/', InvitationView.as_view())
]