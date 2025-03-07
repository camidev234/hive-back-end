from posts.services.post_service import PostService
from posts.serializers.post_reaction_serializers import PostReactionSaveSerializer
from rest_framework import exceptions
from posts.models.post_reaction import PostReaction
from users.services.user_service import UserService

class PostReactionService():
    
    def __init__(self, post_service=None, user_service = None):
        self.post_service = post_service or PostService()
        self.user_service = user_service or UserService()
    
    
    def save_reaction(self, data, user_auth):
        serializer = PostReactionSaveSerializer(data=data)
        
        if serializer.is_valid():
            post = self.post_service.get_post(serializer.validated_data.get("post").id)
            user = self.user_service.get_user(user_auth.id)
            post_reaction = PostReaction()
            
            post_reaction.user = user
            post_reaction.post = post
            post_reaction.reaction_type = "LIKE"
            
            post_reaction.save()
            
            post_reaction_saved = PostReactionSaveSerializer(post_reaction)
            
            return post_reaction_saved.data
        
        raise exceptions.ValidationError(serializer.errors)
    
    def get_post_reactions(self, post_id):
        post = self.post_service.get_post(post_id)
        pass