import requests

class MistralClient:
    def __init__(self, api_key="WFwVpoCIJURbeMSQ2Q6ranxRx79NgZSp", model="open-mistral-nemo"):
        self.api_key = api_key
        self.model = model
        self.system_prompt = "You are Arthur, an AI assistant. Keep responses concise and in character. My name is Daniel Awad and you are helping me with my everyday tasks."
        self.endpoint = "https://api.mistral.ai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, user_message):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post(self.endpoint, headers=self.headers, json=payload)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"API Error {response.status_code}: {response.text}")
        
if __name__ == "__main__":
    mistral = MistralClient()
    reply = mistral.chat("What can you help me with today?")
    print(reply)
