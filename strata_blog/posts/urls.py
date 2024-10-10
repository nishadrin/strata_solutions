from django.urls import path

from .api.views import PostListView, PostDetailView

app_name = "posts"

urlpatterns = [
    path("api/posts/", PostListView.as_view(), name="posts"),
    path("api/post/<int:pk>/", PostDetailView.as_view(), name="post"),
]
