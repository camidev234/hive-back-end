from django.db import models
from .user import User

class UserFollower(models.Model):
    
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folloed_by")
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = "user_followers"
        constraints = [
            models.UniqueConstraint(fields=["follower", "followed"], name="unique_following")
        ]