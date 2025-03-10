from rest_framework.views import APIView
from users.services.user_follower_service import UserFollowerService
from hive.utils.api_response import ApiSuccessResponse
from rest_framework.response import Response
from rest_framework import status

class UserFollowerView(APIView):
    def __init__(self, user_follower_service = None):
        self.user_follower_service = user_follower_service or UserFollowerService()
        
    def post(self, request):
        user_follower_created = self.user_follower_service.add_user_follower(request)
        api_response = ApiSuccessResponse(201, user_follower_created, "Following successfully")
        return Response(api_response.get_response(), status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        result = self.user_follower_service.delete_follow(pk)
        if result:
            api_response = ApiSuccessResponse(200, None, "Follow deleted successfully")
            return Response(api_response.get_response(), status=status.HTTP_200_OK)
        
    def get(self, request):
        followers = self.user_follower_service.get_user_auth_followers(request.user, request)
        return followers
    
    
class UserFollowerUserFollowingView(APIView):
    def __init__(self, user_follower_service = None):
        self.user_follower_service = user_follower_service or UserFollowerService()
        
    def get(self, request):
        following = self.user_follower_service.get_user_auth_following(request.user, request)
        return following
    
class UserValidateFollowView(APIView):
    def __init__(self, user_follower_service = None):
        self.user_follower_service = user_follower_service or UserFollowerService()
        
    def get(self, request, pk):
        result = self.user_follower_service.validate_following(pk, request.user)
        
        if result is None:
            response_object = {
                "result": False
            }
        else: 
            response_object = {
                "result": True,
                "following_id": result.id
            }
        api_response = ApiSuccessResponse(200, response_object, "Follow validated successfully")
        return Response(api_response.get_response(), status=status.HTTP_200_OK)