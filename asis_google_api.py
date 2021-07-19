import speech_recognition as sr
from googletrans import Translator
import playsound
from gtts import gTTS
import random
import time
from time import ctime
import webbrowser
import os
import pyautogui
import pyttsx3


class Person:
    name = ''

    def setname(self, name):
        self.name = name


class Asis:
    name = ''

    def setname(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:


def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            # error: recognizer is not connected
            engine_speak('Sorry, the service is down')
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["hey, how can I help you " + person_obj.name, "hey, what's up? " + person_obj.name, "I'm listening " + person_obj.name, "how can I help you? " + person_obj.name, "hello " + person_obj.name]
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)

    # 2: name person
    if there_exists(["what is my name", "what's my name", "tell me my name"]):
        if person_obj.name:
            engine_speak("your name is " + person_obj.name)
        else:
            engine_speak("i don't know what your name is. tell me your name")

    # 3: name:Assistance
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak("My name is " + asis_obj.name)
        else:
            engine_speak("i don't know what your name is. tell me your name")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setname(person_name)  # remember name in person object

    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setname(asis_name)  # remember name in asis object

    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + " minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # 9 weather
    if there_exists(["what is the weather today"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    # 10 stone paper scissors
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    # 11 toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

    # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(
                int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(
                int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(
                int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(
                int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(
                int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/screenshot/screen.png')

    # 14 to search Use case of
    if there_exists(["Use case of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    if there_exists(["choose any language for translation"]):
        # engine_speak("choose any language among english,french,...")
        voice_data = record_audio("choose any source lang")
        from_lang = voice_data
        engine_speak("You choose source lang...." + from_lang)

        voice_data = record_audio("choose any destination lang")
        to_lang = voice_data
        engine_speak("You choose destination lang " + to_lang)

        voice_data = record_audio("Speak a Sentence...")
        get_sentence = voice_data
        engine_speak("Phase to be Translated :" + get_sentence)

        text_to_translate = Translator().translate(text=get_sentence, dest=to_lang, src=from_lang)
        aa = text_to_translate.text
        engine_speak("Translated Phase:" + aa)

    # Exit
    if there_exists(["exit"]):
        exit()


time.sleep(1)

person_obj = Person()
asis_obj = Asis()
asis_obj.name = 'Alexa'
engine = pyttsx3.init()


while 1:
    voice_data = record_audio("how can I help you")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)  # respond
