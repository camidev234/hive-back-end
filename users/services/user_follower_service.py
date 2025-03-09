from users.serializers.user_follower_serializer import UserFollowerSaveSerializer, UserFollowerAuthFollowers, UserFollowerAuthFollowed
from rest_framework import exceptions
from users.models.user_follower import UserFollower
from users.services.user_service import UserService
from hive.utils.paginator import Paginator

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
        
        return user_following
    
    
    def get_user_follow(self, user_follow_id):
        try:
            user_follow = UserFollower.objects.get(id=user_follow_id)
            return user_follow
        except UserFollower.DoesNotExist:
            raise exceptions.NotFound("The following does not exists")
    
    def delete_follow(self, user_follow_id):
        user_follow = self.get_user_follow(user_follow_id)
        user_follow.delete()
        
        return True
    
    def get_user_auth_followers(self, user_auth, request):
        followers = user_auth.folloed_by.all()
        
        paginator = Paginator(20)
        paginated_followers = paginator.paginate_query_set(followers, request)
        serialized_followers = UserFollowerAuthFollowers(paginated_followers, many=True)
        
        serialized_followers_data = serialized_followers.data
        
        for follower in serialized_followers_data:
            result = self.validate_following(follower["follower"]["id"], user_auth)
            if result is None:
                follower["is_followed"] = False
                follower["following_id"] = None
            else:
                follower["is_followed"] = True
                follower["following_id"] = result.id
        
        paginator_object = paginator.get_paginator_object()
        
        return paginator_object.get_paginated_response(serialized_followers_data)
    
    def get_user_auth_following(self, user_auth, request):
        following = user_auth.following.all()
        
        paginator = Paginator(20)
        paginated_following = paginator.paginate_query_set(following, request)
        serialized_following = UserFollowerAuthFollowed(paginated_following, many=True)
        
        # serialized_followers_data = serialized_followers.data
        
        # for follower in serialized_followers_data:
        #     result = self.validate_following(follower["follower"]["id"], user_auth)
        #     if result is None:
        #         follower["following_id"] = None
        #     else:
        #         follower["following_id"] = result.id
        
        paginator_object = paginator.get_paginator_object()
        
        return paginator_object.get_paginated_response(serialized_following.data)
        
        
        
        