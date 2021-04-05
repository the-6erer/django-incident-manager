from django.contrib import admin
from .models import *
from .forms import *

class IncindentUpdateInline(admin.TabularInline):
    model = IncidentUpdate
    extra = 0
    min_num = 1
    can_delete = False
    def has_change_permission(self, request, obj):
        return False

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'header', 'closed', 'start', 'end')
    search_fields = ['topic', 'header']
    inlines = [
        IncindentUpdateInline,
    ]
    form = IncidentForm
    list_filter = ['closed', 'topic__name']
    
    #disable change after closing incident
    def has_change_permission(self, request, obj=None):
        if obj:
            if obj.closed:
                return False
            else:
                return True
    
    #disable delete after closing incident
    def has_delete_permission(self, request, obj=None):
        if obj:
            if obj.closed:
                return False
            else:
                return True
    
    #do not edit incident after creation
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('topic', 'header', 'impact')
        return self.readonly_fields

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    search_fields = ('header', 'description')
    list_display = ('topic', 'header', 'start', 'end')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification', 'address', 'all_topic', 'get_topics', 'subject')
    form = NotificationForm

    def get_topics(self, obj):
        return ",\n".join([p.name for p in obj.topic.all()])
    get_topics.short_description = 'Topics'

admin.site.site_header = 'Incident Manager'