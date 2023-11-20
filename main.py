import speech_recognition as sr
from createset import valid_phrases

def listen_for_keyword():
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio).lower()
                print(f"Recognized: {text}")

                # Check if the spoken text contains the specified pattern
                if text in valid_phrases:
                    print(f"Wake phrase detected: {text} cannot be countered!")
                    # Perform specific actions here

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    listen_for_keyword()
