from rest_framework.views import APIView
from users.services.auth_service import AuthService
from hive.utils.api_response import ApiSuccessResponse
from rest_framework.response import Response
from rest_framework import status


class AuthView(APIView):
    
    def __init__(self, auth_service=None):
        self.auth_service = auth_service or AuthService()
        
    def post(self, request):
        response = self.auth_service.login(request.data)
        api_response = ApiSuccessResponse(200, response, "User logged in successfully")
        return Response(api_response.get_response(), status=status.HTTP_200_OK)