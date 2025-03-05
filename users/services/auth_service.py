from users.serializers.auth_serializers import LoginSerializer
from users.serializers.user_serializers import UserGetSerializer
from rest_framework import exceptions
from users.models.user import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

class AuthService():
    def login(self, data):
        serializer = LoginSerializer(data=data)
    
        if serializer.is_valid():
            # extract email and password from serializer data
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            # validate email and password
            """
                1. Check if the user exists in the database
                1.1. If the user does not exist, raise an exception with the message 'User not found'
                2. If the user exists, check if the password is correct
                2.1. If the password is incorrect, raise an exception with the message 'Incorrect password
                3. Check if the user is active
                3.1. If the user is inactive, raise an exception with the message 'User is inactive'
            """
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed('User not found')
            if not check_password(password, user.password):
                raise exceptions.AuthenticationFailed('Incorrect password')
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is inactive')
            print("paso validacion de password")
            refresh = RefreshToken.for_user(user)
            user_detail = UserGetSerializer(user).data
            response_object = {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
                "user": user_detail               
            }
            
            
            return response_object
            raise ValidationError(serializer.errors)
        



            
        