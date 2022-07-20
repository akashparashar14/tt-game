from django.db import models
from user_info.models import CustomUser

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
    start_date_of_reg= models.DateTimeField(blank= False, null= True)
    last_date_of_reg = models.DateTimeField(blank=False)
    tournament_start_date = models.DateTimeField()
    tournament_end_date = models.DateTimeField()
    tournament_time = models.TimeField()
    max_score_per_set = models.PositiveIntegerField()
    total_players = models.PositiveIntegerField()
    tournament_type = models.CharField(max_length=50, choices=Tournament_Type, default="private")
    match_type = models.CharField(max_length=50, choices=Match_Type, default="men's single")

    user = models.ManyToManyField(CustomUser, through="tournament_profile_rel")



class tournament_profile_rel(models.Model):
    Request_Accepted =(
    ("accepted" , "Accepted"),
    ("not accepted" , "Not Accepted"),
    ("denied","Denied"),
    )
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_accepted = models.CharField(max_length=50, choices=Request_Accepted, default="accepted")



class Invitation(models.Model):
    

    InviteStatus = (
        (0,"Accepted"),
        (1,"Not_Accepted"),
        (2,"Pending"),  
    )

    status = models.CharField(max_length=20, choices=InviteStatus, default= 2)
    tournament_id = models.ForeignKey(Tournament, related_name="Invitation", on_delete=models.CASCADE, default=None)
    user_id = models.ForeignKey(CustomUser, related_name="User", on_delete=models.CASCADE, default=None)
    from_user = models.ForeignKey(CustomUser, related_name="Form_User",on_delete=models.CASCADE, default=None)
    to_user = models.ForeignKey(CustomUser, related_name="To_User",on_delete=models.CASCADE, default=None)