from django.db import models      
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



# Create your models here

class CustomUser(AbstractUser):

    Gender_choices=(
        ('male','male'),
        ('female','female'),
        ('not specified','not specified')
    )

    Player = (
        ('is_palyer', 'Is Player'),
        ('is_not_player', 'Is Not Player'),
    )

    username = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    gender = models.CharField(max_length=20 ,choices=Gender_choices, default='not specified')
    age = models.IntegerField(default=1)
    photo = models.ImageField(null = True, blank = True)
    match_played = models.IntegerField(default=0)
    match_won = models.IntegerField(default=0)
    played_tournament_name = models.CharField(max_length=200, null=True,blank=True)
    tournament_won = models.CharField(max_length=50, default=0)
    is_player = models.CharField(max_length=20, choices=Player, default='is_player')


    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
