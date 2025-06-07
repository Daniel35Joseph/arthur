from SpeechRecognition.speech_recognition_handler import SpeechRecognitionHandler
from SpeechGeneration.ttsx3_handler import TTSHandler
from AIHandler.mistral_handler import MistralClient

def main():
    mistral_handler = MistralClient()
    speech_recognition_handler = SpeechRecognitionHandler()
    tts_handler = TTSHandler()
    print("Welcome to the Speech Recognition Program!")

    print("Adjusting for ambient noise... Please wait.")
    tts_handler.speak("Adjusting for ambient noise. Please wait.")
    speech_recognition_handler.adjust_ambient_noise(duration=1)
    tts_handler.speak("Hello, this is Arthur, how may I assist you today?")

    while True:
        text = str(speech_recognition_handler.listen_from_microphone())
        print(f"Me: {text}, {type(text)}")

        # Check if the user said "Arthur stop listening"
        if "stop your program" in text.lower():
            print("Stopping the program.")
            tts_handler.speak("Stopping the program. Goodbye!")
            break

        # Check if the text is empty or None
        elif text == "" or text is None or text == "None":
            print("No input detected. Please try again.")
            tts_handler.speak("No input detected. Please try again.")
        
        # Check if the text is valid
        elif text != None and text != "" and text is not None:
            try:
                response = mistral_handler.chat(text)
                print(f"Arthur: {response}")
                tts_handler.speak(response)
            except Exception as e:
                print(f"Error: {e}")
                tts_handler.speak("Sorry, I encountered an error while processing your request.")

if __name__ == "__main__":
    main()