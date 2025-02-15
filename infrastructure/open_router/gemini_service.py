import os
import requests
import json

from models.study_guide import StudyGuide


class GeminiService:
    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = os.getenv("OPENROUTER_API_KEY")

    def generate_study_guide(self, topic: str) -> str:
        if not topic:
            raise ValueError("Topic cannot be empty")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "google/gemini-exp-1206:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Generate a study guide about: {topic}"
                        }
                    ]
                }
            ]
        }

        try:
            
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            print(response.json())
            return json.dumps(response.json(), indent=4)
        except requests.exceptions.RequestException as e:
            return json.dumps({"error": str(e)})
