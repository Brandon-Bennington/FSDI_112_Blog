from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # List all posts at /posts/
    path('new/', PostCreateView.as_view(), name='post_new'),  # Create a new post at /posts/new/
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # View details of a post at /posts/1/
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Edit a post at /posts/1/edit/
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete a post at /posts/1/delete/
]
