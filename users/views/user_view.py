from rest_framework.views import APIView
from rest_framework.response import Response
from users.services.user_service import UserService
from hive.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from rest_framework import status

class UserView(APIView):
    def __init__(self, user_service=None):
        super().__init__()
        self.user_service = user_service or UserService()
        
    def post(self, request):
        user_saved = self.user_service.save_user(request.data)
        response_data = ApiSuccessResponse(201, user_saved, "User created successfully")
        return Response(response_data.get_response(), status=status.HTTP_201_CREATED)
        