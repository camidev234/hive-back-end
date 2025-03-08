from users.serializers.user_serializers import SaveUserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from users.models.user import User
from rest_framework import exceptions
from users.services.profile_service import ProfileService
from django.db import transaction
# from users.serializers.profile_serializers import ProfileGetSerializer

class UserService():
    
    def __init__(self, profile_service = None):
        self.profile_service = profile_service or ProfileService()
    
    @transaction.atomic
    def save_user(self, user_data):
        """
        Guarda un usuario y su perfil asociado de manera atómica.
        """
        serializer = SaveUserSerializer(data=user_data)
        if serializer.is_valid():
            try:
                if 'password' in user_data:
                    serializer.validated_data["password"] = make_password(user_data["password"])
                
                user_saved = serializer.save()
                
                self.profile_service.save_profile(user_saved)
                
                user_serialized = SaveUserSerializer(user_saved)
                
                return user_serialized.data

            except Exception as e:
                raise ValidationError(f"Error to save the user and Profile: {str(e)}")
        
        raise ValidationError(serializer.errors)
    
    def get_user(self, user_id):
        try:
            user_found = User.objects.get(id=user_id)
            return user_found
        except User.DoesNotExist:
            raise exceptions.NotFound("The user does not found")