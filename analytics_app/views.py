# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.db.models import Count
from .models import EventLog
from .serializers import EventLogSerializer

def home(request):
    return render(request, 'index.html')

# def home(request):
#     return HttpResponse("🚀 Django Analytics API is Running")

# POST /api/events/
class EventLogView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            EventLog.objects.create(
                user=request.user,
                event_type=serializer.validated_data['event_type'],
                button_name=serializer.validated_data.get('button_name')
            )
            return Response({"message": "Event logged"})
        return Response(serializer.errors, status=400)


# GET /api/analytics/summary/
class AnalyticsSummaryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "total_events": EventLog.objects.count(),
            "total_button_clicks": EventLog.objects.filter(event_type='button_click').count(),
            "total_logins": EventLog.objects.filter(event_type='login').count(),
        })


# GET /api/analytics/buttons/
class ButtonAnalyticsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = (
            EventLog.objects
            .filter(event_type='button_click')
            .values('button_name')
            .annotate(total_clicks=Count('id'))
        )
        return Response(data)