from posts.serializers import post_serializers
from rest_framework import exceptions
from posts.models.post import Post
from hive.utils.paginator import Paginator
from posts.serializers.post_serializers import PostGetSerializer

class PostService():
    def save_post(self, user_auth, post_data):
        serializer = post_serializers.PostSaveSerializer(data=post_data)
        
        if serializer.is_valid():
            post_to_save = Post()
            post_to_save.title = serializer.validated_data.get("title")
            post_to_save.content = serializer.validated_data.get("content")
            post_to_save.user_id = user_auth.id 
            
            post_to_save.save()
            
            post_saved = post_serializers.PostSaveSerializer(post_to_save)
            
            return post_saved.data
        
        raise exceptions.ValidationError(serializer.errors)
    
    def get_posts(self, request):
        posts = Post.objects.all().exclude(user_id=request.user.id).order_by("-created_at")
        paginator = Paginator(30)
        paginated_posts = paginator.paginate_query_set(posts, request)
        
        serialized_posts = PostGetSerializer(paginated_posts, many=True)
        
        paginator_object = paginator.get_paginator_object()
        
        return paginator_object.get_paginated_response(serialized_posts.data)
    
    def get_post(self, post_id):
        try:
            post_found = Post.objects.get(id=post_id)
            return post_found
        except Post.DoesNotExist:
            raise exceptions.NotFound(f"The post {post_id} does not found")