import requests
# from config import mistral_free_api_key
mistral_free_api_key = "WFwVpoCIJURbeMSQ2Q6ranxRx79NgZSp"
assistant_stop_command = "stop your program"

class MistralClient:
    """A client for interacting with the Mistral AI API."""

    def __init__(self, api_key=mistral_free_api_key, model="open-mistral-nemo"):
        """ Initializes the MistralClient with the provided API key and model.
        Args:
            api_key (str): The API key for accessing the Mistral AI service.
            model (str): The model to use for generating responses. Default is "open-mistral-nemo".
        Raises:
            ValueError: If the API key is not provided.
            Exception: If the API key is invalid or the model is not supported.
        """
        # Parameters:
        self.api_key = api_key
        self.model = model
        self.endpoint = "https://api.mistral.ai/v1/chat/completions"
        self.system_prompt = "You are Arthur, an AI assistant. Keep responses concise and in character. My name is Daniel Awad and you are helping me with my everyday tasks."
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.conversation_history = []
        self.initialize_conversation()

    def initialize_conversation(self):
        """Initialize or reset the conversation history"""
        self.conversation_history = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, user_message):
        """Generates a response from the Mistral AI based on the user's message.
        Args:
            user_message (str): The message from the user to which the AI will respond.
        Returns:
            str: The AI's response to the user's message.
        Raises:
            Exception: If the API request fails or returns an error.
        """
        # Validate the user message
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_message}
            ]
        }

        # Make the API request
        response = requests.post(self.endpoint, headers=self.headers, json=payload)
        
        # Check the response status and return the content
        if response.status_code == 200:
            # Parse and return the AI's response
            return response.json()["choices"][0]["message"]["content"]
        else:
            # Raise an exception if the API request fails
            raise Exception(f"API Error {response.status_code}: {response.text}")

    def generate_response(self, user_input, continue_conversation=True):
        """Generate a response while optionally maintaining conversation context"""
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        payload = {
            "model": self.model,
            "messages": self.conversation_history
        }

        response = requests.post(
            self.endpoint, 
            headers=self.headers, 
            json=payload
        )
        
        if response.status_code == 200:
            assistant_response = response.json()["choices"][0]["message"]["content"]
            # Add assistant's response to history if continuing conversation
            if continue_conversation:
                self.conversation_history.append(
                    {"role": "assistant", "content": assistant_response}
                )
            return assistant_response
        else:
            raise Exception(f"API Error {response.status_code}: {response.text}")

    def new_conversation(self, initial_message):
        """Start a new conversation with an initial message"""
        self.initialize_conversation()
        return self.generate_response(initial_message)

    def continue_conversation(self, user_message):
        """Continue existing conversation with a new message"""
        return self.generate_response(user_message)

    def get_conversation_history(self):
        """Return the current conversation history"""
        return self.conversation_history

if __name__ == "__main__":
    """Entry point for testing the MistralClient."""
    # Test the MistralClient by sending a sample message
    mistral = MistralClient()
    reply = mistral.chat("What can you help me with today?")
    print(reply)

# Example usage
if __name__ == "__main__":
    # Initialize the client
    mistral = MistralClient()
    
    # Start a new conversation
    print("Starting new conversation...")
    reply = mistral.initialize_conversation()
    print("AI:", reply)
    
    # Continue the conversation
    reply = mistral.continue_conversation("Can you help me with Python programming?")
    print("AI:", reply)