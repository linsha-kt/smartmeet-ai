from meetings.models import Meeting
from datetime import timedelta
from django.utils import timezone


class WeeklyReportService:

    def get_last_week_meetings(self):

        last_week = timezone.now() - timedelta(days=7)

        meetings = Meeting.objects.filter(
            created_at__gte=last_week
        )

        return meetings