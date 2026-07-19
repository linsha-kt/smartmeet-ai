from django.db import models
from meetings.models import Meeting


class AIResult(models.Model):

    STATUS_CHOICES = (

        ("pending", "Pending"),

        ("processing", "Processing"),

        ("completed", "Completed"),

        ("failed", "Failed"),

    )

    meeting = models.OneToOneField(
        Meeting,
        on_delete=models.CASCADE,
        related_name="ai_result"
    )

    transcript = models.TextField(
        blank=True,
        null=True
    )

    summary = models.TextField(
        blank=True,
        null=True
    )

    key_decisions = models.TextField(
        blank=True,
        null=True
    )

    action_items = models.TextField(
        blank=True,
        null=True
    )

    processing_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"AI Analysis - {self.meeting.title}"