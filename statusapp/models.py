from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.conf import settings
from rest_framework.authtoken.models import Token

class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)

class Maintenance(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return "%s" % (self.header)

class Incident(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    IMPACT_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    impact = models.CharField(max_length=50, choices=IMPACT_CHOICES, default='MEDIUM')

    def __str__(self):
        return "%s" % (self.header)

class IncidentUpdate(models.Model):
    STATUS_CHOICES = [
        ('IDENTIFIED', 'Identified'),
        ('INVESTIGATING', 'Investigating'),
        ('RESOLVED', 'Resolved'),
    ]
    incident = models.ForeignKey('Incident', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return "%s - %s" % (self.status, self.description)

class Notification(models.Model):
    NOTIFY_CHOICES = [
        ('TEAMS', 'Microsoft Teams'),
        ('EMAIL', 'Email'),
    ]
    SUBJECT_CHOICES = (
        ('INCIDENT', 'Incident'),
        ('MAINTENANCE', 'Maintenance'),
    )
    notification = models.CharField(max_length=50, choices=NOTIFY_CHOICES)
    address = models.CharField(max_length=400, help_text='Enter Incoming Webhook URL or Email address depending on the notification type')
    topic = models.ManyToManyField('Topic', blank=True)
    all_topic = models.BooleanField(default=False, verbose_name="All topics", help_text='If selected, above topics will automatically be unselected')
    subject = MultiSelectField(choices=SUBJECT_CHOICES, default='Incident')
    
    def __str__(self):
        return "%s - %s" % (self.notification, self.address)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=IncidentUpdate, dispatch_uid="IncidentUpdate Alert")
def send_alert(sender, instance, created, **kwargs):
    if created:
        incident = instance.incident
        if not incident.start:
            incident.start = instance.timestamp
            incident.save()
        if 'RESOLVED' in instance.status:
            if not incident.end:
                incident.end = instance.timestamp
            incident.closed = True
            incident.save()
        notifylist = Notification.objects.filter(topic = instance.incident.topic) | Notification.objects.filter(all_topic = True)
        for notify in notifylist:
            if notify.notification == 'TEAMS':
                alertTeams(instance, notify)
            elif notify.notification == 'EMAIL':
                alertEmail(instance, notify)

def alertTeams(instance, notify):
    print("Teams")

def alertEmail(instance, notify):
    print("Mail")