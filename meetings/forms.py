from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):

    class Meta:

        model = Meeting

        fields = [
            "title",
            "description",
            "participants",
            "meeting_date",
            "duration",
            "audio_file",
            "status",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

            "participants": forms.SelectMultiple(
                attrs={
                    "class": "form-select"
                }
            ),

            "meeting_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "audio_file": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }