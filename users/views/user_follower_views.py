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