from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.Home.as_view()),
    path('notification/', views.NotificationList.as_view()),
    path('notification/<int:pk>/', views.NotificationDetail.as_view()),
    path('maintenance/', views.MaintenanceList.as_view()),
    path('topic/', views.TopicList.as_view()),
    path('incident/', views.IncidentList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)