from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post_new'),  # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # View details of a specific post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Edit a specific post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete a specific post
]
