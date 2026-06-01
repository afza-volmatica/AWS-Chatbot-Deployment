import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/chat"

MODEL_NAME = "qwen2.5:1.5b"


def get_llm_response(user_message: str):

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]

    except Exception as e:
        return f"Error communicating with Ollama: {e}"