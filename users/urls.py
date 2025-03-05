from django.urls import path
from users.views.user_view import UserView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
]