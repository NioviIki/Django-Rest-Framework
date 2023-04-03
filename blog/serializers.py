from blog.models import Comments, Posts

from rest_framework import serializers


class PostSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Posts
        fields = ['url', 'id', 'subject', 'text', 'date', 'owner', 'comments']


class CommentsSerializers(serializers.HyperlinkedModelSerializer):
    owners = serializers.ReadOnlyField(source='owner.username')
    post_text = serializers.ReadOnlyField(source='post.text')

    class Meta:
        model = Comments
        fields = ['url', 'id', 'text', 'date', 'post_text', 'post', 'owners']
