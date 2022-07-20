from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        validated_data ['password'] = make_password(validated_data ['password'])
        user = CustomUser.objects.create(**validated_data)
        return user

        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('gender','age','username','first_name','last_name','email')
    
    def create(self, validated_data):
        print(validated_data)
        validated_data ['password'] = make_password(validated_data ['password'])
        user = CustomUser.objects.create(**validated_data)
        return user

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('gender','age','username','first_name','last_name',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    # password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance



