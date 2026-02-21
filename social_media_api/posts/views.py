from rest_framework import viewsets, permissions, filters, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        # Create notification for post author when someone comments
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb='commented on your post',
                target_content_type=ContentType.objects.get_for_model(comment.post),
                target_object_id=comment.post.id,
            )


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id,
            )

        return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'error': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)