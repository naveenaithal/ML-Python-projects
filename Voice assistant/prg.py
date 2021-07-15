from  neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer=speech_recognition.Recognizer()

speaker=tts.init()
speaker.setProperty('rate',150)

todo_list=['shoppin','playing','learning new concepts of python']

def creat_note():
    global recognizer
    speaker.say('What do you want to write in your note')
    speaker.runAndWait()
    done=False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note=recognizer.recognize_google(audio)
                note=note.lower()

                speaker.say("Choose a file name")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename=recognizer.recognize_google(audio)
                filename= filename.lower()

                with open(f'{filename}.txt','w') as f:
                    f.write(note)
                    done=True
                    speaker.say(f"Sucessfully created {filename}")
                    speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("i dint understand please try again")
            speaker.runAndWait()


def add_todo():
    global recognizer
    speaker.say('What you want to add to your todo')
    speaker.runAndWait()

    done=False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio=recognizer.listen(mic)

                item=recognizer.recognize_google(audio)
                item=item.lower()

                todo_list.append(item)
                done=True
                speaker.say(f"{item} added to to do list")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("I didn't get you please try again")
            speaker.runAndWait()


def show_todo():

    speaker.say("The items on your to do list as follows")
    speaker.runAndWait()
    for item in todo_list:
        speaker.say(item)
        speaker.runAndWait()

def hello():
    speaker.say("Hello what can i do for you")
    speaker.runAndWait()

def quit():
    speaker.say("Bye see you again!")
    speaker.runAndWait()
    sys.exit(0)

mappings={"greetings":hello,
          "create note": creat_note,
          "add todo": add_todo,
          "show todo": show_todo,
          "bye":quit


}
assistant=GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()
            assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer=speech_recognition.Recognizer()
        speaker.say("Couldn't here you try again")
        speaker.runAndWait()











