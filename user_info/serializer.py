from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','email','name','password']
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
                phone_number=profile_data['phone_number'],
                age=profile_data['age'],
                gender=profile_data['gender']
        )
            return user
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'