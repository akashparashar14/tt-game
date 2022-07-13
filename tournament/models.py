from django.db import models
from datetime import datetime
# Create your models here.


class Tournament(models.Model):
    Match_Type=(
    ("men's single" , "Men's Single"),
    ("women's single" , "Women's Single"),
    ("men's double" , "Men's Double"),
    ("women's double" , "Women's Double"),
    ("double" , "Double"),
    )

    Tournament_Type= (
    ("public" , "Public"),
    ("private" , "Private"),
    )

    tournament_name = models.CharField(max_length=250)
    start_date_of_reg= models.DateField(blank= False)
    last_date_of_reg = models.DateField(blank=False)
    tournament_start_date = models.DateField()
    tournament_end_date = models.DateField()
    tournament_time = models.DateTimeField()
    max_score_per_set = models.PositiveIntegerField()
    total_players = models.PositiveIntegerField()
    tournament_type = models.CharField(max_length=50, choices=Tournament_Type, default="private")
    match_type = models.CharField(max_length=50, choices=Match_Type, default="men's single")
    
# class tournament_profile_rel(models.Model):
#     Request_Accepted =(
#     ("accepted" , "Accepted"),
#     ("not accepted" , "Not Accepted"),
#     )
#     profile = models.ForeignKey("user_info.User", on_delete=models.CASCADE)
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
#     # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     is_accepted = models.CharField(max_length=50, choices=Request_Accepted, default="accepted")