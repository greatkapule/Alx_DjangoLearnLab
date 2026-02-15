from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, PostByTagListView
)

urlpatterns = [
    # Existing Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Tagging and Search URL Patterns
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]