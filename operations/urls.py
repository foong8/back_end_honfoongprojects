from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, AssignmentViewSet, QcticketViewSet, QClogViewSet, UserViewSet,TicketNoteViewSet

router=DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('country', CountryViewSet, basename='country')
router.register('qcticket', QcticketViewSet, basename='qcticket')
router.register('qclog', QClogViewSet, basename='qclog')
router.register('assignment', AssignmentViewSet, basename='assignment')
router.register('ticketnote', TicketNoteViewSet, basename='ticketnote')

urlpatterns=[
    path('',include(router.urls)),
]
