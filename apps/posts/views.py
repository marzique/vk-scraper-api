from rest_framework import viewsets
from rest_framework import permissions

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """TODO"""

    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  

