from rest_framework import serializers
from posts.models.post_reaction import PostReaction
from posts.models.post import Post
from users.serializers.user_serializers import UserGetSerializer

class PostReactionSaveSerializer(serializers.ModelSerializer):
    
    post_id = serializers.PrimaryKeyRelatedField(
        queryset = Post.objects.all(),
        source = "post",
        required = True
    )
    
    user_id = serializers.PrimaryKeyRelatedField(
        source = "user",
        read_only = True
    )
    
    class Meta:
        model = PostReaction
        fields = ["id", "post_id", "user_id", "created_at"]
        
class ReactionGetSerializer(serializers.ModelSerializer):
    
    user_id = serializers.PrimaryKeyRelatedField(
        source = "user",
        read_only = True
    )
    
    class Meta:
        model = PostReaction
        fields = ["id", "post_id", "reaction_type", "user_id"]
        
class ReactionDeleteSerializer(serializers.Serializer):
    
    post_reaction_id = serializers.IntegerField(required=True)    
    
class ReactionGetListSerializer(serializers.ModelSerializer):
    
    user = UserGetSerializer()
    
    class Meta:
        model = PostReaction
        fields = ["id", "post_id", "reaction_type", "user", "created_at"]
    
    
    