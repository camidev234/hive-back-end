from django.db import models
from .post import Post
from django.db.models import UniqueConstraint
from users.models.user import User

class PostReaction(models.Model):
    
    REACTION_CHOICES = [
        ("LIKE", "Like"),
        
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    reaction_type = models.CharField(
        max_length=10,
        choices=REACTION_CHOICES,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "post_reactions"
        constraints = [
            UniqueConstraint(fields=['user', 'post'], name='unique_user_post_reaction')
        ]
    