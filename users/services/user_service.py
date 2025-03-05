from users.serializers.user_serializers import SaveUserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

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