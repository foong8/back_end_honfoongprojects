from django.contrib.auth.models import User

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
# from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from .models import Post, Comment,ActionItem,Progress,HistoryLog



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            "id",
            "username",
            "is_active",
        ) 

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    # reviewer=UserSerializer(read_only=True) 
    # approver=UserSerializer(read_only=True)
    # assignee=UserSerializer(read_only=True)
    country_tag = TagListSerializerField()
    class Meta:
        model=Post
        fields='__all__'

class GetPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    requester=UserSerializer(read_only=True)
    reviewer=UserSerializer(read_only=True)
    approver=UserSerializer(read_only=True)
    assignee=UserSerializer(read_only=True)
    country_tag = TagListSerializerField()
    class Meta:
        model=Post
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields='__all__'

class GetCommentSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    
    class Meta:
        model=Comment
        fields='__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Progress
        exclude = ('content', 'created_at')

class GetProgressSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    class Meta:
        model=Progress
        exclude = ('content', 'created_at')

class ActionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActionItem
        fields='__all__'

class GetActionItemSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    
    class Meta:

        model=ActionItem
        fields='__all__'

class HistoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoryLog
        fields='__all__'

class GetHistoryLogSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    
    class Meta:

        model=HistoryLog
        fields='__all__'