# modules/llm_interface.py
import requests

def call_llm(prompt):
    headers = {
        "Authorization": "de3MaxMVwIqHZTSxsqVcRVxvmdaZDMUK",  # 👈 把這裡換成你的
        "Content-Type": "application/json"
    }
    payload = {
        "model": "google/gemma-3-12b-it",
        "messages": [
            {"role": "system", "content": "你是一個有溫度的AI助理。"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.deepinfra.com/v1/openai/chat/completions",
                             headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
