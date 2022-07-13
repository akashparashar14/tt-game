from django.contrib import admin
from .models import CustomUser, tournament_profile_rel
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(tournament_profile_rel)