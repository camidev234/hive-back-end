from rest_framework.views import APIView
from posts.services.post_reaction_service import PostReactionService
from rest_framework.permissions import IsAuthenticated
from hive.utils.api_response import ApiSuccessResponse
from rest_framework.response import Response
from rest_framework import status

class PostReactionView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, post_reaction_service = None):
        self.post_reaction_service = post_reaction_service or PostReactionService()
        
    def post(self, request):
        post_reaction = self.post_reaction_service.save_reaction(request.data, request.user)
        api_response = ApiSuccessResponse(201, post_reaction, "Reaction created successfully")
        return Response(api_response.get_response(), status=status.HTTP_201_CREATED)
        
     