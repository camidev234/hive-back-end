from users.serializers.user_follower_serializer import UserFollowerSaveSerializer
from rest_framework import exceptions
from users.models.user_follower import UserFollower
from users.services.user_service import UserService

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
    
    def validate_following(self, user_id, user_auth):
        user_service = UserService()
        
        user = user_service.get_user(user_id)
        
        user_following = user_auth.following.filter(followed_id=user.id).first()
        
        if user_following is None:
            return False
        
        return True