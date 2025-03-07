from rest_framework.urls import path
from posts.views import post_views, post_reaction_views

urlpatterns = [
    path("posts/", post_views.PostView.as_view(), name="posts"),
    path("reactions/", post_reaction_views.PostReactionView.as_view(), name="reactions")
]