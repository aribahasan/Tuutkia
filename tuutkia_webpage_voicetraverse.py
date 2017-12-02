import webbrowser
import string
import speech_recognition as sr

#Record Audio
r = sr.Recognizer()
#Recognizes voice from Microphone
with sr.Microphone() as source:
        print("****Welcome to Tuutkia Voice Webpage Traversing****")
        print("What Tuutkia web page do u want to open?")
        print("Main Page? or Sign Up?")
        print("Say webpage name")
        #recording voice
        audio = r.listen(source)
        print ("I'm Listening....")
        try:
            text = r.recognize_google(audio)
            print("You asked me to open:" + text)
            if text == "main page" in r.recognize_google(audio):
                r2 = sr.Recognizer()
                url = 'https://www.tuutkia.com/'
                with sr.Microphone() as source:
                    print ("Opening Tuutkia website")
                    print ("Welcome to Tuutkia" + r2.recognize_google(webbrowser.open_new(url)))
            elif text == "sign up" in r.recognize_google(audio):
                r3 = sr.Recognizer()
                url = 'https://www.theleadsxchange.com/signUp'
                with sr.Microphone() as source:
                    print("Opening Sign Up Page" + r3.recognize_google(webbrowser.open_new(url)))
            else:
                print("Audio could not be understood")
                print ("Sorry! Please say it clearly the next time")
        except Exception as e:
            print ("No voice detected, please try again")






