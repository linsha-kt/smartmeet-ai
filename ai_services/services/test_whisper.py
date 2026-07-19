from ai_services.services.whisper_service import WhisperService

whisper_service = WhisperService()

text = whisper_service.transcribe(
    "media/meeting_audio/sample.mp3"
)

print(text)