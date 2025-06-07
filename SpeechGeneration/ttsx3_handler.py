import pyttsx3

class TTSHandler:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.default_voice = self.voices[0].id
        self.default_rate = 150
        self.default_volume = 1.0
        
    def set_voice(self, voice_index):
        """Set voice by index (0 for default, 1 for alternative if available)"""
        if 0 <= voice_index < len(self.voices):
            self.engine.setProperty('voice', self.voices[voice_index].id)
            return True
        return False
    
    def set_rate(self, rate):
        """Set speech rate (words per minute)"""
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """Set volume (0.0 to 1.0)"""
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)
            return True
        return False
    
    def speak(self, text):
        """Speak the given text"""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def list_available_voices(self):
        """Return list of available voices"""
        return [(i, voice.name) for i, voice in enumerate(self.voices)]
    
    def save_to_file(self, text, filename):
        """Save speech to an audio file"""
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()

if __name__ == "__main__":
    tts = TTSHandler()
    
    # Example usage
    print("Available voices:", tts.list_available_voices())
    tts.set_rate(150)
    tts.set_volume(0.8)
    tts.speak("Hello, this is a test using the TTS Handler class")
    
    # Save to file example
    # tts.save_to_file("This is a test of saving to file", "test_output.mp3")
    