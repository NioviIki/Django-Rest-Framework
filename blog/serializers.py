from blog.models import Comments, Posts

from django.contrib.auth.models import Group, User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Posts
        fields = ['url', 'id', 'subject', 'text', 'date', 'owner',]


class CommentsSerializers(serializers.HyperlinkedModelSerializer):
    owners = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comments
        fields = ['url', 'id', 'text', 'date', 'post', 'owners']
