from rest_framework import serializers
from users.models.user_follower import UserFollower
from users.models.user import User

class UserFollowerSaveSerializer(serializers.ModelSerializer):
    
    followed_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = "followed",
    )
    
    follower_id = serializers.PrimaryKeyRelatedField(
        source="follower",
        read_only=True
    )
    
    class Meta:
        model = UserFollower
        fields = ["id", "follower_id" ,"followed_id", "created_at"]