from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from users.models.user import User

class SaveUserSerializer(ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["name", "last_name", "username", "email", "born_date", "password", "gender"]
        
class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "last_name", "username", "email", "born_date", "gender", "created_at", "updated_at"]