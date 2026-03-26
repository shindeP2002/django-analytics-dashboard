from django.urls import path
from .views import EventLogView, AnalyticsSummaryView, ButtonAnalyticsView

urlpatterns = [
    path('events/', EventLogView.as_view()),
    path('analytics/summary/', AnalyticsSummaryView.as_view()),
    path('analytics/buttons/', ButtonAnalyticsView.as_view()),
]