from django.db import models
from users.models.user import User

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(max_length=450, blank=True, null=True)
    image_url = models.CharField(max_length=400, blank=True, null=True)
    
    
    class Meta:
        db_table = "profiles"