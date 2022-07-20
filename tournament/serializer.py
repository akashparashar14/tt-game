from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Tournament, Invitation

class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ("__all__")

class TournamentViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ("__all__")
    
    def create(self, validated_data):
        user = Tournament.objects.create(**validated_data)
        return user


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        models = Invitation
        fields = ('from_user','to_user','tournament_id','status',)

        def create(self, validated_data):
            return Invitation.objects.create(**validated_data)

class UpdateTournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('tournament_name','start_date_of_reg','last_date_of_reg','tournament_start_date','tournament_end_date'
                    ,'match_type','tournament_type')