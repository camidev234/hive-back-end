from rest_framework.views import APIView
from posts.services.post_service import PostService
from hive.utils.api_response import ApiSuccessResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class PostView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, post_service=None):
        self.post_service = post_service or PostService()
        
    def post(self, request):
        post_saved = self.post_service.save_post(request.user, request.data)
        api_response = ApiSuccessResponse(201, post_saved, "Post Created Succesffully")
        return Response(api_response.get_response(), status=status.HTTP_201_CREATED)