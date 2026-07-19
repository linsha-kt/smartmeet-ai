from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from meetings.models import Meeting
from .models import AIResult
from .services.ai_processor import AIProcessor


def generate_ai(request, meeting_id):

    meeting = get_object_or_404(
        Meeting,
        id=meeting_id
    )

    try:

        processor = AIProcessor()

        result = processor.process_meeting(meeting)

        AIResult.objects.update_or_create(

            meeting=meeting,

            defaults={

                "transcript": result["transcript"],

                "summary": result["summary"],

                "key_decisions": result["key_decisions"],

                "action_items": result["action_items"],

                "processing_status": "completed",

            }

        )

        messages.success(
            request,
            "AI Analysis Generated Successfully."
        )

    except Exception as e:

        messages.error(
            request,
            str(e)
        )

    return redirect(
        "ai_report",
        meeting_id=meeting.id
    )


def ai_report(request, meeting_id):

    meeting = get_object_or_404(
        Meeting,
        id=meeting_id
    )

    ai_result = AIResult.objects.filter(
        meeting=meeting
    ).first()

    return render(
        request,
        "ai_services/report.html",
        {
            "meeting": meeting,
            "ai_result": ai_result,
        }
    )