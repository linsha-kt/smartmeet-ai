import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiService:

    def __init__(self):

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def analyze_meeting(self, transcript):

        prompt = f"""
You are an AI Meeting Assistant.

Before analyzing the meeting:

- Remove filler words such as "um", "uh", "ah", "hmm", "erm".
- Ignore repeated words and unnecessary pauses.
- Correct minor grammar mistakes.
- Preserve the original meaning.
- Keep names, dates, and technical terms unchanged.

Analyze the cleaned meeting transcript.

Return ONLY valid JSON.

Format:

{{
    "summary": "...",

    "key_decisions": [
        "...",
        "..."
    ],

    "action_items": [
        "...",
        "..."
    ]
}}

Transcript:

{transcript}

Do not return markdown.
Do not return explanations.
Return JSON only.
"""

        try:

            response = self.model.generate_content(
                prompt
            )

            text = response.text.strip()

            # Remove Markdown code block if present
            text = text.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            ).strip()

            return json.loads(text)

        except json.JSONDecodeError:

            return {

                "summary": "Unable to parse AI response.",

                "key_decisions": [],

                "action_items": []

            }

        except Exception as e:

            return {

                "summary": f"Gemini Error: {str(e)}",

                "key_decisions": [],

                "action_items": []

            }