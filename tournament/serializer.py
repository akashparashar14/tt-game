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
        fields = ('user_id','tournament_id','status',)

        def create(self, validated_data):
            return Invitation.objects.create(**validated_data)