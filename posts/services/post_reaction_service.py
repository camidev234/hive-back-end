from posts.services.post_service import PostService
from posts.serializers.post_reaction_serializers import PostReactionSaveSerializer, ReactionDeleteSerializer, ReactionGetListSerializer
from rest_framework import exceptions
from posts.models.post_reaction import PostReaction
from users.services.user_service import UserService
from hive.utils.paginator import Paginator
from users.services.user_follower_service import UserFollowerService

class PostReactionService():
    
    def __init__(self, post_service=None, user_service = None, user_follower_service=None):
        self.post_service = post_service or PostService()
        self.user_service = user_service or UserService()
        self.user_follower_service = user_follower_service or UserFollowerService()
    
    
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
    
    def get_post_reaction(self, reaction_id):
        try:
            post_reaction_found = PostReaction.objects.get(id=reaction_id)
            return post_reaction_found
        except PostReaction.DoesNotExist:
            raise exceptions.NotFound("The reaction does not exists")
    
    def delete_reaction(self, pk):
        
        post_reaction = self.get_post_reaction(pk)
        post_reaction.delete()
        return True
    
    
    def get_post_reactions(self, post_id, request):
        post = self.post_service.get_post(post_id)
        reactions = PostReaction.objects.filter(post_id=post_id).order_by("-created_at")
        
        paginator = Paginator(20)
        paginated_reactions = paginator.paginate_query_set(reactions, request)
        serialized_reactions = ReactionGetListSerializer(paginated_reactions, many=True)
        
        reactions_data = serialized_reactions.data
        
        for reaction in reactions_data:
            result = self.user_follower_service.validate_following(reaction["user"]["id"], request.user)
            if result is None:
                reaction["is_followed"] = False
                reaction["following_id"] = None
            else:
                reaction["is_followed"] = True
                reaction["following_id"] = result.id
        
        paginator_object = paginator.get_paginator_object()
        
        return paginator_object.get_paginated_response(reactions_data)
        
        
        