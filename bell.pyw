import winsound
import datetime
import ast
import webbrowser
import time
import pyttsx3
engine = pyttsx3.init()

def bell():
    winsound.PlaySound("bellsound", winsound.SND_FILENAME)

def say(phrase):
    engine.say(phrase)
    engine.runAndWait()
    
    
say("Auto join has started")
a=1
x=0


while a<2:
    file = open("belltimes.txt", "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    now = datetime.datetime.now()
    weekday = datetime.datetime.now().strftime("%A")
    for w in dictionary['times'][weekday]:
        x = dictionary['times'][weekday][w]
        hour = int(x[:2])
        minute = int(x[2:])
        if hour == now.hour and minute == now.minute and 4 >= now.second:
            webbrowser.open(dictionary['links'][w])
            time.sleep(6)
    time.sleep(0.1)
