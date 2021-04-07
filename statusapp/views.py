from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic.base import TemplateView
from .services import *
import json

class IncidentList(generics.ListAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,]
    #permission_classes = [IsAuthenticated]
    
    serializer_class = IncidentSerializer
    def get_queryset(self):
        queryset = Incident.objects.filter(closed=False)
        status = self.request.GET.get('status','').lower()
        if status:
            if status == 'all':
                queryset = Incident.objects.all()
            elif status == 'open':
                queryset = Incident.objects.filter(closed=False)
            elif status == 'closed':
                queryset = Incident.objects.filter(closed=True)
        else:
            return queryset
        return queryset

class MaintenanceList(generics.ListAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,]
    #permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationList(generics.ListCreateAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication,]
    #permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    def get_queryset(self):
        queryset = Notification.objects.all()
        notification = self.request.GET.get('notification','').lower()
        address = self.request.GET.get('address','').lower()
        if notification and address:
            queryset = Notification.objects.filter(notification=notification, address=address)
        elif notification:
            queryset = Notification.objects.filter(notification=notification)
        elif address:
            queryset = Notification.objects.filter(address=address)
        return queryset

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        incidents = callGetEndpoint('incident')
        topics = callGetEndpoint('topic')

        print(incidents)

        for topic in topics:
            t_id = topic['id']
            
        
        #context['incidents'] = callGetEndpoint('incident')
        #context['maintenances'] = callGetEndpoint('maintenance')
        return context