from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        depth = 1
        fields = ['id', 'notification', 'address', 'topic', 'all_topic', 'subject']

        serializers.UniqueTogetherValidator(
            queryset=Notification.objects.all(),
            fields=('notification', 'address'),
            message=("Notification with this Notification and Address already exists.")
        )

class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentUpdate
        fields = ['id', 'incident', 'status', 'description', 'timestamp']
        #fields = ['incident']

class IncidentSerializer(serializers.ModelSerializer):
    #incidents = serializers.StringRelatedField(many=True)
    incident_updates = IncidentUpdateSerializer(many=True)
    class Meta:
        model = Incident
        depth = 1
        fields = "__all__"
        #fields = ['id', 'topic', 'header', 'start', 'end', 'closed', 'impact', 'incident_updates']

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'topic', 'header', 'start', 'end']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        #fields = ['id', 'name']
        fields = "__all__"