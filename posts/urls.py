from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet,ProgressViewSet,ActionItemViewSet, HistoryLogViewSet

router=DefaultRouter()
router.register('progress', ProgressViewSet, basename='progress')
router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')
router.register('actionitem', ActionItemViewSet, basename='actionitem')
router.register('historylog', HistoryLogViewSet, basename='historylog')

urlpatterns=[
    path('',include(router.urls)),
]