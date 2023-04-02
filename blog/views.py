from rest_framework import viewsets
from .serializers import PostSerializers, CommentsSerializers
from .models import Posts, Comments

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers

