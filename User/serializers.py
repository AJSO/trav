from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

class NewUserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name','phone','password')




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        print(refresh['user_id'])
        # extra responses
        userid = refresh['user_id']
        email = self.user.email
        # user = User.objects.get(refresh['user_id'])

        abc = User.objects.filter(id = userid).values('email', 'phone', 'full_name')
        
        print (abc)
        data['user'] = abc

        return data