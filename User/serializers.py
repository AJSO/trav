from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
User = get_user_model()

class NewUserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name','phone','password')