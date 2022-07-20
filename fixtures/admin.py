from django.contrib import admin
from .models import Fixtures, Set_Scores
# Register your models here.

@admin.register(Fixtures)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('match_date','match_round','player_id_home','player_id_away')

@admin.register(Set_Scores)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('set_no','player_id_home_score','player_id_away_score')