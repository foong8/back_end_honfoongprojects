from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Country,Assignment,Qcticket,Qclog,QcLogNote
from .serializer import UserSerializer,CountrySerializer,AssignmentSerializer,QcticketSerializer,QClogSerializer, GetQcticketSerializer,TicketNoteSerializer,GetTicketNoteSerializer

from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class=CountrySerializer
    queryset=Country.objects.all()

    def perform_create(self, serializer):
        pass

    def perform_update(self, serializer):
        pass
    
    def retrieve(self, request, *args, **kwargs):
        pass
    
    def destory(self, request, *args, **kwargs):
        pass

    @action(detail=True, methods=['GET'])
    def custom_function(self, request, *args, **kwargs):
        pass

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class=AssignmentSerializer
    queryset=Assignment.objects.all()

    # def perform_create(self, serializer):
    #     pass

    # def perform_update(self, serializer):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass
    
    # def destory(self, request, *args, **kwargs):
    #     pass

    # @action(detail=True, methods=['GET'])
    # def custom_function(self, request, *args, **kwargs):
    #     pass

class QcticketViewSet(viewsets.ModelViewSet):
    serializer_class=QcticketSerializer
    queryset = Qcticket.objects.all()

    def get_serializer_class(self):
        if self.action in ["list"]:
            return GetQcticketSerializer
        return QcticketSerializer

    def get_queryset(self):
        if "filter_type" in self.request.GET:
            if self.request.GET["filter_type"] == "TicketQueuePendingUpdate":
                return self.queryset.filter(status="Completed").filter(qcresult="Has_Error").filter(mistaked_made_by__isnull=True)
            
            elif self.request.GET["filter_type"] == "TicketQueueUpdated":
                return self.queryset.filter(status="Completed").filter(qcresult="Has_Error").filter(mistaked_made_by__isnull=False)

            elif self.request.GET["filter_type"] == "TicketQueueCompleted":
                return self.queryset.filter(status="Completed")
            
            elif self.request.GET["filter_type"] == "TicketQueueInQueue":
                return self.queryset.filter(status="In_Queue")
        
        elif "filter_date" in self.request.GET:
            if self.request.GET["filter_date"]== "Today":
                today=datetime.today().strftime('%Y-%m-%d')
                return self.queryset.filter(created_at__gt=today)
            if self.request.GET["filter_date"]== "This_Month":
                this_year=datetime.today().strftime('%Y')
                this_month=datetime.today().strftime('%m')
                return self.queryset.filter(created_at__year=this_year,
                                            created_at__month=this_month,)
            elif self.request.GET["filter_date"]== "This_Year":
                this_year=datetime.today().strftime('%Y')
                return self.queryset.filter(created_at__year=this_year)
        else:
            return self.queryset

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data)

    def perform_update(self, serializer):
        member_id = self.request.data['mistake_made_by']
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(mistaked_made_by=user)

class QClogViewSet(viewsets.ModelViewSet):
    serializer_class=QClogSerializer
    queryset=Qclog.objects.all()

class TicketNoteViewSet(viewsets.ModelViewSet):
    serializer_class=TicketNoteSerializer
    queryset=QcLogNote.objects.all()

    def get_serializer_class(self):
        if self.action in ["list"]:
            return GetTicketNoteSerializer
        return TicketNoteSerializer

    def get_queryset(self):
        ticket_id=self.request.GET.get('ticket_id')
        return self.queryset.filter(note_id=ticket_id)

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save()
        return Response(serializer.data)

