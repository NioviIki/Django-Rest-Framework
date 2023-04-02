from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, PostSerializers, CommentsSerializers
from .models import Posts, Comments


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    # permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    # permission_classes = [permissions.IsAuthenticated]