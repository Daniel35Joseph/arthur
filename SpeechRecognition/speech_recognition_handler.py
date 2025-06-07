import speech_recognition as sr
from SpeechGeneration.ttsx3_handler import TTSHandler
from typing import Optional

class SpeechRecognitionHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_handler = TTSHandler()

    def listen_from_microphone(self, timeout: int = None, phrase_time_limit: int = None) -> Optional[str]:
        """
        Listen to audio input from microphone and convert to text
        """
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
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
        """
        try:
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
                
            try:
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
        """
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=duration)