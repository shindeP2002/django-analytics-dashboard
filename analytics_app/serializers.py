from rest_framework import serializers
from .models import EventLog

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ['event_type', 'button_name']

    def validate(self, data):
        if data['event_type'] == 'button_click' and not data.get('button_name'):
            raise serializers.ValidationError("button_name is required")
        return data