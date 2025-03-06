from rest_framework import serializers
from posts.models.post import Post
from users.models.user import User

class PostSaveSerializer(serializers.ModelSerializer):
    
    user_id = serializers.PrimaryKeyRelatedField(
        source = "user",
        read_only = True
    )
    
    class Meta:
        model = Post
        fields = ["title", "content", "user_id"]