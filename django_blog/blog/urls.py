from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # Changed to /posts/
    path('posts/new/', PostCreateView.as_view(), name='post-create'), # Changed to /posts/new/
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # Changed to /posts/<int:pk>/
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'), # Changed to /edit/
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Changed to /delete/
]