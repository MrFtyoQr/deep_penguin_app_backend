import os
import requests
import json

from models.study_guide import StudyGuide


class GeminiService:
    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.api_key = os.getenv("OPENROUTER_API_KEY")

    def generate_study_guide(self, topic: str, level: str, style: str) -> str:
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
                            "text": f"Genera una guía de estudio en formato JSON basada en el tema: {topic}, nivel:{level} y hazlo de un estilo {style}. el key:text del objeto principal debe ser un texto que ayude a responder las preguntas \
                                    El JSON debe seguir esta estructura:\n\n\
                                    {{'text': str, 'questions': list[{{'text': str, 'options': list[{{'index': int, 'text': str}}], 'correct_answer': {{'index': int, 'text': str}} }}]}}\n\n\
                                    Devuelve solo el JSON sin explicaciones ni texto adicional,sin marcas de formato como '```json`'."
                        }
                    ]
                }
            ]
        }

        try:
            
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            text_response = response.json()["choices"][0]["message"]["content"]
            return text_response.replace("```json", "").replace("```", "").strip()
        except requests.exceptions.RequestException as e:
            return json.dumps({"error": str(e)})
