from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


from rest_framework import viewsets, status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment, Progress, ActionItem, HistoryLog
from .serializer import UserSerializer,PostSerializer,GetPostSerializer,CommentSerializer,GetCommentSerializer, \
                        ProgressSerializer, GetProgressSerializer, ActionItemSerializer, GetActionItemSerializer, \
                        HistoryLogSerializer, GetHistoryLogSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GetPostSerializer
        return PostSerializer

    def get_queryset(self):
        if "filter_cat" in self.request.GET:
            if self.request.GET["filter_cat"] == "System_Change_Request":
                return self.queryset.filter(category="System_Change_Request")
            elif self.request.GET["filter_cat"] == "System_Bug":
                return self.queryset.filter(category="System_Bug")
            elif self.request.GET["filter_cat"] == "General":
                return self.queryset.filter(category="General")
            elif self.request.GET["filter_cat"] == "Ad_Hoc_Requests":
                return self.queryset.filter(category="Ad_Hoc_Requests")
            elif self.request.GET["filter_cat"] == "Routine_Tasks":
                return self.queryset.filter(category="Routine_Tasks")
        else:
            return self.queryset

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

    def perform_update(self, serializer):
        # instance = self.get_object()  # instance before update
        # a = self.request.data.get("approver", None)  # read data from request
        # print(a)
        # print(serializer['approver'])
        # print(instance.approver)
        
        # print(type(self.request.data))

        serializer.save()
        
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GetCommentSerializer
        return CommentSerializer

    def get_queryset(self):
        
        post_id=self.request.GET.get('post_id')
        print(post_id)
        if post_id:
            return self.queryset.filter(post_id=post_id)
        else:
            return self.queryset

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class=ProgressSerializer
    queryset=Progress.objects.all()

    def get_serializer_class(self):
        if self.action in ["list"]:
            return GetProgressSerializer
        return ProgressSerializer

    def get_queryset(self):
        post_id=self.request.GET.get('post_id')
        return self.queryset.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

class ActionItemViewSet(viewsets.ModelViewSet):
    
    serializer_class=ActionItemSerializer
    queryset=ActionItem.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GetActionItemSerializer
        return ActionItemSerializer

    def get_queryset(self):
        post_id=self.request.GET.get('post_id')
        if post_id:
            return self.queryset.filter(post_id=post_id)
        else:
            return self.queryset

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

class HistoryLogViewSet(viewsets.ModelViewSet):
    
    serializer_class=HistoryLogSerializer
    queryset=HistoryLog.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GetHistoryLogSerializer
        return HistoryLogSerializer

    def get_queryset(self):
        post_id=self.request.GET.get('post_id')
        if post_id:
            return self.queryset.filter(post_id=post_id)
        else:
            return self.queryset

    def perform_create(self, serializer):
        
        print(serializer)
        serializer.save()
        return Response(serializer.data)