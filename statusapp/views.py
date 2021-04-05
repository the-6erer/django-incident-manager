from .models import *
from .serializers import *
from rest_framework import generics
#from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class IncidentUpdateList(generics.ListAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = IncidentUpdateSerializer
    def get_queryset(self):
        incidents = list(Incident.objects.all().values_list('id', flat=True))
        return IncidentUpdate.objects.filter(id__in=incidents)

class IncidentList(generics.ListAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class IncidentOpenList(generics.ListAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Incident.objects.filter(closed=False)
    serializer_class = IncidentSerializer

class NotificationList(generics.ListAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationCreate(generics.CreateAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        print("Bla")
        form = self.form_class(request.POST)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer