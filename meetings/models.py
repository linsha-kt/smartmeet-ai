from django.db import models
from accounts.models import User


class Meeting(models.Model):

    STATUS_CHOICES = (

        ("uploaded", "Uploaded"),

        ("processing", "Processing"),

        ("completed", "Completed"),

    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True,
        null=True
    )


    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_meetings"
    )


    participants = models.ManyToManyField(
        User,
        related_name="attended_meetings",
        blank=True
    )


    meeting_date = models.DateTimeField()


    duration = models.IntegerField(
        blank=True,
        null=True
    )


    audio_file = models.FileField(
        upload_to="meeting_audio/",
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="uploaded"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title