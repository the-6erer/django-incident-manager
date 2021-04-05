from rest_framework import serializers
#from rest_framework.validators import UniqueTogetherValidator
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        depth = 2
        fields = ['id', 'notification', 'address', 'topic', 'all_topic', 'subject']

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        depth = 2
        fields = ['id', 'topic', 'header', 'start', 'end', 'closed', 'impact']

class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentUpdate
        depth = 2
        fields = ['id', 'incident', 'status', 'description', 'timestamp']
