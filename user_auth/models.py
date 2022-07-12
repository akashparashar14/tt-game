from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from tournament.models import Tournament

# Create your models here.

class Profile (models.Model):
    Gender_Choice = (
    (0,'male'),
    (1,'female'),
    (2,'not specified'),
    )
    # user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40,default='Leave Blank',unique = True)
    email_id = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=40)
    gender = models.IntegerField(choices=Gender_Choice)
    age = models.IntegerField()
    photo = models.ImageField(upload_to = 'images')
    match_played = models.IntegerField()
    match_won = models.IntegerField()
    played_tournament_name = models.CharField(max_length=200)
    tournament_won = models.CharField(max_length=200)
    is_player = models.BooleanField()

    tournament = models.ManyToManyField(Tournament, through="tournament_profile_rel")

class tournament_profile_rel(models.Model):
    Request_Accepted =(
    ("accepted" , "Accepted"),
    ("not accepted" , "Not Accepted"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_accepted = models.CharField(max_length=50, choices=Request_Accepted, default="accepted")

    


