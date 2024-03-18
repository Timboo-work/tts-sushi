import dependencies
import speech_recognition
import text_to_speech
import config

def main():
    dependencies.check_and_install_dependencies()
    recognized_text = speech_recognition.recognize_speech()
    if recognized_text:
        text_to_speech.synthesize_speech(recognized_text)

if __name__ == "__main__":
    main()
