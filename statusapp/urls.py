from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get_notifications/', views.NotificationList.as_view()),
    path('add_notification/', views.NotificationCreate.as_view()),
    path('get_incidents/', views.IncidentList.as_view()),
    path('get_open_incidents/', views.IncidentOpenList.as_view()),
    path('get_incident_updates/', views.IncidentUpdateList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)