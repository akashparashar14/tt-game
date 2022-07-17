from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }


        def create(self, validated_data):
            profile_data = validated_data.pop('profile')
            user = CustomUser.objects.create_user(**validated_data)
            CustomUser.objects.create(
                user=user,
                first_name=profile_data['first_name'],
                last_name=profile_data['last_name'],
                age=profile_data['age'],
                gender=profile_data['gender']
        )
            return user

        

        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        validated_data ['password'] = make_password(validated_data ['password'])
        user = CustomUser.objects.create(**validated_data)
        return user



class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('gender','age','username',)