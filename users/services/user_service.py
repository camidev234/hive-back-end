from users.serializers.user_serializers import SaveUserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from users.models.user import User
from rest_framework import exceptions

class UserService():
    def save_user(self, user_data):
        serializer = SaveUserSerializer(data=user_data)
        if serializer.is_valid():
            if 'password' in user_data:
                serializer.validated_data["password"] = make_password(user_data["password"])
            user_saved = serializer.save()
            user_serialized = SaveUserSerializer(user_saved)
            return user_serialized.data
        
        raise ValidationError(serializer.errors)
    
    def get_user(self, user_id):
        try:
            user_found = User.objects.get(id=user_id)
            return user_found
        except User.DoesNotExist:
            raise exceptions.NotFound("The user does not found")