from django.contrib import admin
from .models import Tournament, Invitation, tournament_profile_rel
# Register your models here.

@admin.register(Tournament)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('tournament_name','start_date_of_reg','tournament_start_date','tournament_type')

@admin.register(tournament_profile_rel)
class TournamentRelationAdmin(admin.ModelAdmin):
    list_display = ('profile','tournament')
                                           
# @admin.register(Invitation)
# class InviteAdmin(admin.ModelAdmin):
#     list_display = ('tournament_id','status')

    