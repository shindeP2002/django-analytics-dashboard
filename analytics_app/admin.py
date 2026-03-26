from django.contrib import admin
from .models import EventLog, UserProfile

admin.site.register(EventLog)
admin.site.register(UserProfile)