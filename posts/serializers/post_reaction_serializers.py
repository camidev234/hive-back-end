from rest_framework import serializers
from posts.models.post_reaction import PostReaction
from posts.models.post import Post

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