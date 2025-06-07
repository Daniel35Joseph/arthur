import speech_recognition as sr
from SpeechGeneration.ttsx3_handler import TTSHandler
from typing import Optional

from config import assistant_stop_command

class SpeechRecognitionHandler:
    def __init__(self):
        """Initialize the speech recognition handler with recognizer and microphone"""
        # Initialize the speech recognizer and microphone
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_handler = TTSHandler()

    def listen_from_microphone(self, timeout: int = None, phrase_time_limit: int = None) -> Optional[str]:
        """
        Listen to audio input from microphone and convert to text
        Args:
            timeout (int): Maximum time to wait for speech input
            phrase_time_limit (int): Maximum time for a phrase to be spoken
        Returns:
            Optional[str]: Recognized text from the audio input, or None if recognition fails
        """
        try:
            # Listen to the microphone input
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            # Recognize the speech in the audio
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
                return None
                
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def recognize_from_file(self, audio_file: str) -> Optional[str]:
        """
        Convert audio file to text
        Args:
            audio_file (str): Path to the audio file
        Returns:
            Optional[str]: Recognized text from the audio file, or None if recognition fails
        """
        # Check if the audio file exists
        try:
            # Open the audio file and recognize speech
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
                
            try:
                # Recognize the speech in the audio file
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Could not understand audio file")
                return None
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
                return None
                
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def adjust_ambient_noise(self, duration: int = 1):
        """
        Adjust recognizer for ambient noise
        Args:
            duration (int): Duration in seconds to adjust for ambient noise
        """
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=duration)
            return True
        except Exception as e:
            print(f"Error adjusting for ambient noise: {e}")
            return False

if __name__ == "__main__":
    # Entry point for the speech recognition program
    speech_recognition_handler = SpeechRecognitionHandler()
    print("Welcome to the Speech Recognition Program!")

    # Adjust ambient noise for better recognition
    print("Adjusting for ambient noise... Please wait.")
    speech_recognition_handler.adjust_ambient_noise(duration=1)

    # The while loop to continuously listen for user input
    while True:
        # Listen for user input from the microphone
        print("Recognizing speech...")
        text = str(speech_recognition_handler.listen_from_microphone())
        print(text)

        # Check if the user said "Arthur stop listening"
        if assistant_stop_command.lower() in text.lower():
            print("Stopping the program.")
            break