from django.urls import path
from users.views.user_view import UserView
from users.views.auth_views import AuthView
from users.views.custom_refresh_view import CustomTokenRefreshView
from users.views.user_follower_views import UserFollowerView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path("auth/login/", AuthView.as_view(), name="login"),
    path("auth/refresh/", CustomTokenRefreshView.as_view(), name="refresh"),
    path("usersfollowing/", UserFollowerView.as_view(), name="user_followers")
]