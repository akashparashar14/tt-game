from django.db import models


# Create your models here 

class Fixtures(models.Model):
    Level = (
    ('round_1','Round 1'),
    ('round_2','SemiFinal'),
    ('round_3','Final')
) 
    match_date = models.DateTimeField()
    match_round =  models.CharField(max_length=50, choices=Level, default="round_1")
    player_id_home = models.CharField(max_length=200)
    player_id_away = models.CharField(max_length=250)

class Set_Scores(models.Model):
    set_no = models.IntegerField()
    player_id_home_score = models.IntegerField()
    player_id_away_score = models.IntegerField()