from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class OnlineModelHandler:
    def __init__(self, model_name="facebook/opt-350m"):
        """Initialize with a smaller model that works well online"""
        print(f"Loading model {model_name}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self.system_prompt = "You are Arthur, an AI assistant similar to JARVIS from Iron Man. Keep responses concise and in character."

    def generate_response(self, user_input):
        """Generate a response for the given user input"""
        formatted_prompt = f"{self.system_prompt}\nUser: {user_input}\nArthur:"
        
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.model.device)
        
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.2,
            pad_token_id=self.tokenizer.eos_token_id
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("Arthur:")[-1].strip()

    def __call__(self, prompt):
        return self.generate_response(prompt)


if __name__ == "__main__":
    # Example usage
    handler = OnlineModelHandler()
    response = handler.generate_response("What's the weather like today?")
    print(response)