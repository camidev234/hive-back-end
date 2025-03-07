from django.db import models
from users.models.user import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "posts"