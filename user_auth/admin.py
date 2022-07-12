from django.contrib import admin
from .models import Profile,tournament_profile_rel

# Register your models here.
admin.site.register(Profile)
admin.site.register(tournament_profile_rel)