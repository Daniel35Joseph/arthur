from sppech_recognition_handler import SpeechRecognitionHandler

def main():
    speech_recognition_handler = SpeechRecognitionHandler()
    print("Welcome to the Speech Recognition Program!")

    print("Adjusting for ambient noise... Please wait.")
    speech_recognition_handler.adjust_ambient_noise(duration=1)

    while True:
        
        print("Recognizing speech...")
        text = speech_recognition_handler.listen_from_microphone()
        if "arthur stop listening" in text.lower():
            print("Stopping the program.")
            break

if __name__ == "__main__":
    main()