import speech_recognition as sr
print ("Do you want to record notes?")
print("Press 'y' to record notes OR Press 'n' to Quit")
input = raw_input("type y or n and press enter:   ")
if input == 'y':

    #Record Audio
    r = sr.Recognizer()
    #Recognizes voice from Microphone
    with sr.Microphone() as source:
            print("Recording........")
            #recording voice
            audio = r.listen(source)
            print ("I'm Listening....")
            try:
                notes = r.recognize_google(audio)
                print("Your notes are:\n" + notes)

            except Exception as e:
                print("This is an exception")
            except sr.UnknownValueError:
                print ("Could not understand Audio")
            except sr.RequestError as e:
                print ("Could not request result {0}" .format(e))
if input == 'n':
    print("You've quit the recording!")



