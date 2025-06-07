# Library imports
from SpeechRecognition.speech_recognition_handler import SpeechRecognitionHandler
from SpeechGeneration.ttsx3_handler import TTSHandler
from AIHandler.mistral_handler import MistralClient

# File imports
from config import assistant_stop_command

def main():
    """Main function to run the speech recognition program."""
    # Initialize handlers
    mistral_handler = MistralClient()
    speech_recognition_handler = SpeechRecognitionHandler()
    tts_handler = TTSHandler()

    # Adjust ambient noise for better recognition
    print("Adjusting for ambient noise... Please wait.")
    tts_handler.speak("Adjusting for ambient noise. Please wait.")

    # Adjust ambient noise for the speech recognition handler
    speech_recognition_handler.adjust_ambient_noise(duration=1)
    tts_handler.speak("Hello, this is Arthur, how may I assist you today?")

    # Main loop to listen for user input
    while True:
        # Listen for user input from the microphone
        text = str(speech_recognition_handler.listen_from_microphone())
        print(f"Me: {text}, {type(text)}")

        # Check if the user said "Arthur stop listening"
        if assistant_stop_command in text.lower():
            # Stop the program if the user says "stop your program"
            print("Stopping the program.")
            tts_handler.speak("Stopping the program. Goodbye!")
            break

        # Check if the text is empty or None
        elif text == "" or text is None or text == "None":
            # If no input is detected, prompt the user to try again
            print("No input detected. Please try again.")
            tts_handler.speak("No input detected. Please try again.")
        
        # Check if the text is valid
        elif text != None and text != "" and text is not None:
            # Process the text with the Mistral AI handler
            try:
                # Generate a response using the Mistral AI handler
                response = mistral_handler.chat(text)
                print(f"Arthur: {response}")
                tts_handler.speak(response)
            except Exception as e:
                # Handle any exceptions that occur during processing
                print(f"Error: {e}")
                tts_handler.speak("Sorry, I encountered an error while processing your request.")

if __name__ == "__main__":
    """"Entry point for the speech recognition program."""
    # Run the main function
    main()