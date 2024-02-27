from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'meetings_attended', 'event', 'cohort', '')

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'meetings_attended', 'password', 'event', 'cohort', 'tshirt', 'grade', 'decaid')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'meetings_attended', 'event', 'cohort', 'tshirt', 'grade', 'decaid')
        
    def validate_password(self, value):
        validate_password(value)
        return value

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

