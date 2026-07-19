import whisper
import re


class WhisperService:

    def __init__(self):

        self.model = whisper.load_model("base")

    def clean_transcript(self, text):

        # Common filler words
        fillers = [
            "um", "umm", "uh", "ah", "hmm", "hmmm",
            "erm", "like", "you know", "okay", "ok"
        ]

        # Remove filler words
        for word in fillers:
            text = re.sub(
                rf"\b{re.escape(word)}\b",
                "",
                text,
                flags=re.IGNORECASE
            )

        # Remove repeated punctuation
        text = re.sub(r"\.{2,}", ".", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def transcribe(self, audio_path):

        result = self.model.transcribe(audio_path)

        transcript = result["text"]

        cleaned_transcript = self.clean_transcript(
            transcript
        )

        return cleaned_transcript