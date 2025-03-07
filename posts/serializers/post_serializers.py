from rest_framework import serializers
from posts.models.post import Post
from users.models.user import User
from users.serializers.user_serializers import UserGetSerializer

class PostSaveSerializer(serializers.ModelSerializer):
    
    user_id = serializers.PrimaryKeyRelatedField(
        source = "user",
        read_only = True
    )
    
    class Meta:
        model = Post
        fields = ["id", "title", "content", "user_id"]
        
class PostGetSerializer(serializers.ModelSerializer):
    
    user = UserGetSerializer()
    
    class Meta:
        model = Post
        fields = ["id", "title", "content", "user", "created_at", "updated_at"]