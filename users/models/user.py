from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo de email debe ser proporcionado.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) 
        return user
    

class User(AbstractBaseUser):
    
    STATUS_CHOICES = [
        ("MASCULINO", "Masculino"),
        ("FEMENINO", "Femenino"),
        ("OTRO", "Otro")
    ]
    
    
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=250)
    # password = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        null=False,
        blank=False
    )
    born_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'username', 'born_date', 'gender']
    
    objects = UserManager()
    
    class Meta:
        db_table = 'users'