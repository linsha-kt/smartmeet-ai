from django.urls import path
from . import views

urlpatterns = [

    path(
        "generate/<int:meeting_id>/",
        views.generate_ai,
        name="generate_ai",
    ),

    path(
        "report/<int:meeting_id>/",
        views.ai_report,
        name="ai_report",
    ),

]