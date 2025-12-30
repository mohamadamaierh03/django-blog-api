from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class PostSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Post
        fields = '__all__'