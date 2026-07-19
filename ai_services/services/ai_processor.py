from .whisper_service import WhisperService
from .gemini_service import GeminiService


class AIProcessor:

    def __init__(self):

        self.whisper = WhisperService()

        self.gemini = GeminiService()

    def process_meeting(self, meeting):

        # Convert speech to text
        transcript = self.whisper.transcribe(
            meeting.audio_file.path
        )

        # Analyze transcript using Gemini
        analysis = self.gemini.analyze_meeting(
            transcript
        )

        # Return the processed data
        return {

            "transcript": transcript,

            "summary": analysis.get(
                "summary",
                ""
            ),

            "key_decisions": "\n".join(
                analysis.get(
                    "key_decisions",
                    []
                )
            ),

            "action_items": "\n".join(
                analysis.get(
                    "action_items",
                    []
                )
            )

        }