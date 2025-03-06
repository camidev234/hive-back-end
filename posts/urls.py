from rest_framework.urls import path
from posts.views import post_views

urlpatterns = [
    path("posts/", post_views.PostView.as_view(), name="posts"),
]