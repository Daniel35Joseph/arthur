from SpeechRecognition.speech_recognition_handler import SpeechRecognitionHandler
from SpeechGeneration.ttsx3_handler import TTSHandler
import time

def main():
    speech_recognition_handler = SpeechRecognitionHandler()
    tts_handler = TTSHandler()
    print("Welcome to the Speech Recognition Program!")
    tts_handler.speak("Welcome to the Speech Recognition Program!")

    print("Adjusting for ambient noise... Please wait.")
    tts_handler.speak("Adjusting for ambient noise. Please wait.")
    speech_recognition_handler.adjust_ambient_noise(duration=1)

    while True:
        # tts_handler.speak("Listening")
        text = str(speech_recognition_handler.listen_from_microphone())
        print(text)
        if "arthur stop listening" in text.lower():
            print("Stopping the program.")
            break

if __name__ == "__main__":
    main()