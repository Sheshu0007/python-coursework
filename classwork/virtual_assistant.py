import speech_recognition as sr
import pyttsx3



engine=pyttsx3.init()

def speak(text):
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()



def listen():
    recogniser=sr.Recognizer()
    with sr.Microphone() as source:
        print("listining")
        recogniser.pause_threshold=1
        audio=recogniser.listen(source)

        try:
            command=recogniser.recognize_google(audio,language="en-in")
            print("listening",command)
            return command.lower()
        except sr.UnknownValueError:
            print("sorry i didnt listen")
            speak("sorry i didnt get you")
            return""
        except sr.RequestError:
            print("the server is not working")
            speak("the server is down")
            return""

speak("Hello sir how can i help you")

while True:
    command=listen()
    if "hi" in command:
        speak("hello sheshu,  how are you ")
        speak("how can i help you")
    elif "set alarm" in command:
        speak("are you that much lazy")
        speak("i think you should do it bye your self")
    elif "weather" in command:
        speak("Ohhh you want to know about the weather, open the window check it ")
    elif "stop"in command or "bye" in command:
        speak("good to know byee")
        break
    else:
     speak(" I didnt get it, come again")