from users.serializers.user_follower_serializer import UserFollowerSaveSerializer
from rest_framework import exceptions
from users.models.user_follower import UserFollower

class UserFollowerService():
    def add_user_follower(self, request):
        serializer = UserFollowerSaveSerializer(data=request.data)
        
        if serializer.is_valid():
            new_follower = UserFollower()
            
            new_follower.follower = request.user
            new_follower.followed = serializer.validated_data.get("followed")
            
            new_follower.save()
            
            return UserFollowerSaveSerializer(new_follower).data
            
        raise exceptions.ValidationError(serializer.errors)