from django.contrib import admin
from .models import EventLog, UserProfile

@admin.register(EventLog)
class EventLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'button_name', 'timestamp')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state')