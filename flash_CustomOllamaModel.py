# enter the master's name here ------ #
mastername = "Saksham"
model_of_your_choice_on_ollama = ''  # ENTER YOUR MODEL FO YOUR CHOICE KEEPING YOUR PC SPECS IN MIND HERE BEFORE USING MODEL...otherwise AI features won't work

import pyttsx3 
import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO
import datetime
import os
import cv2
import requests
from requests import get
import webbrowser as wb
from keyboard import press
import time
import pywhatkit as kit
import sys 
import winsound
import pyjokes  
import threading
import pyautogui
from pywikihow import search_wikihow
import psutil
import random
import geocoder
import requests
import json
import ollama

pygame.init()
pygame.mixer.init()

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id)

# text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def speak_with_gtts(text, language='en', tld='co.in'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        return ""
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning sir, flash is online, kaya would be working in background")
    elif hour>=12 and hour<16:
        speak("good afternoon sir, flash is online, kaya would be working in background")
    else: speak("good evening sir, flash is online, kaya would be working in background")

#def set_reminder(reminder, seconds):
    #def reminder_thread():
        #speak(f"Setting a reminder for {reminder} in {seconds} seconds.")
        #time.sleep(seconds)
        #speak(f"Reminder: {reminder}")

    #thread = threading.Thread(target=reminder_thread)
    #thread.start()


def batterycheck():
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        if plugged:
            pass
        else:
            if percent<=15 and percent>10:
                speak_with_gtts("low battery, please connect the charger")
                time.sleep(400)
            if percent<=10:
                speak_with_gtts("battery is critically low, please connect the charger")
                time.sleep(300)
thread_batterycheck = threading.Thread(target=batterycheck)  # threading alarm to work in background
thread_batterycheck.daemon = True
thread_batterycheck.start()

def alarm(query_for_alarm):
    t = query_for_alarm.replace("wake me up after", "").replace("wake me up in", "").replace("set alarm for", "").replace("hours", "").replace("hour", "").replace("minutes", "").replace("minute", "").replace("seconds", "").replace("second", "").replace("flash", "")
    t = int(t)
    if "seconds" in query_for_alarm or "second" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} seconds")
        time.sleep(t)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300)
        speak_with_random_responsegtts("alarm")
    if "minutes" in query_for_alarm or "minute" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} minutes")
        time.sleep(t*60)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300) 
        speak_with_random_responsegtts("alarm")
    if "hours" in query_for_alarm or "hour" in query_for_alarm:
        speak_with_gtts(f"sure, I'll ring the bell in {t} hours")
        time.sleep(t*3600)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300)
        time.sleep(0.2)
        winsound.Beep(900, 300)
        speak_with_random_responsegtts("alarm")

def typewrite():
    print("INITIATING TYPEWRITE")
    while True:

        text = takecommand().lower()

        if "backspace" in text:
            pyautogui.hotkey("ctrl", "backspace")
        if "clear all" in text or "delete all" in text:
            pyautogui.hotkey("ctrl","a")
            time.sleep(1)
            pyautogui.press("backspace")
        if "stop typing" in text:
            speak("ok")
            break
        else:
            pyautogui.write(text, interval=0.1)

def screen_navigation():
    speak("initiating screen navigation")
    #speak("pls take care of any surrounding noise for better functionality")
    while True:
        q = takecommand().lower()
        if any(x in q for x in ["stop navigating", "stop navigation", "exit screen navigation", "exit navigation"]):
            speak("ok")
            break
        if "start typing" in q:
            typewrite()
        for command in commands_for_pyautogui:
            if f"press {command[0]}".lower() in q.lower():
                pyautogui.press(command[1])
            if f"hold {command[0]}".lower() in q.lower():
                pyautogui.keyUp(command[1])
            if f"release {command[0]}".lower() in q.lower():
                pyautogui.keyDown(command[1])
            if "close this window" in q:
                pyautogui.hotkey("alt", "f4")

def purge():  # clears screen...
    os.system('cls' if os.name == 'nt' else 'clear')

def location():
    g = geocoder.ip('me')
    print(g.latlng)

def speak_with_random_responsegtts(key):
    response = random.choice(responses[key])
    speak_with_gtts(response)

def speak_with_random_responsepyttsx(key):
    response = random.choice(responses[key])
    speak(response)

responses = {
    "welcome": ["my pleasure master", "always ready to help sir", "no worries master", "always there for you sir"],
    "goodbye": ["kk, standbye", "goodbye sir, see you soon", "wake me up when needed sir", "thanks, I was a bit tired"],
    "joke": ["here's a joke", "I hope this makes you laugh", "my non-emotional voice is funny already, anyways here's a joke"],
    "hello": ["hello sir, I'm up", "Hi sir, what can I do for you", "I'm right here, ready to help", "I am at your service, Master.", "It's good to have you back, Master.", "It is a pleasure to see you, Master."],
    "iamup": ["I'm up and working fine", "I can't sleep without your permission hence I'm up", "I don't remember you asking me to sleep"],
    "alarm": ["knock knock, this is the alarm beep", "wake up!! it's time", "don't worry it's not system making sounds, it's me cause the alarm time is up", "Beep beep! It's time to wake up. This is your wake-up call!", "Ding ding! Wakey wakey! The alarm is going off!"],
}

commands_for_pyautogui = [
    ["!", "!"],
    ["hashtag", "#"],
    ["dollar", "$"],
    ["percentage", "%"],
    ["and", "&"],
    ["plus", "+"],
    ["0", "0"],
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["colon", ":"],
    ["semi colon", ";"],
    ["lesser than", "<"],
    ["equal", "="],
    ["greater than", ">"],
    ["question mark", "?"],
    ["at the rate", "@"],
    ["add", "add"],
    ["alt", "alt"],
    ["alternate", "alt"],
    ["backspace", "backspace"],
    ["browser back", "browserback"],
    ["browser forward", "browserforward"],
    ["caps lock", "capslock"],
    ["control", "ctrl"],
    ["dot", "decimal"],
    ["point", "decimal"],
    ["delete", "delete"],
    ["divide", "divide"],
    ["down", "down"],
    ["end", "end"],
    ["enter", "enter"],
    ["escape", "escape"],
    ["F1", "f1"], ["F2", "f2"], ["F3", "f3"], ["F4", "f4"], ["F5", "f5"],
    ["F6", "f6"], ["F7", "f7"], ["F8", "f8"], ["F9", "f9"], ["F10", "f10"],
    ["F11", "f11"], ["F12", "f12"],
    ["left", "left"],
    ["multiply", "multiply"],
    ["num lock", "numlock"],
    ["page down", "pagedown"],
    ["page up", "pageup"],
    ["print screen", "prtscr"],
    ["right", "right"],
    ["separator", "separator"],
    ["shift", "shift"],
    ["shiftleft", "shiftleft"],
    ["shiftright", "shiftright"],
    ["space", "space"],
    ["subtract", "subtract"],
    ["tab", "tab"],
    ["up", "up"],
    ["volumedown", "volumedown"],
    ["mute", "volumemute"],
    ["volumeup", "volumeup"],
    ["windows", "win"],
]

sites = [

    # Entertainment & Media
    ["netflix", "https://www.netflix.com"],
    ["spotify", "https://www.spotify.com"],
    ["movie", "https://vipstream.tv"],

    # Communication & Email
    ["mailbox", "https://mail.google.com/mail/u/0/#inbox"],

    # Social Media
    ["facebook", "https://www.facebook.com"],
    ["instagram", "https://www.instagram.com"],
    ["twitter", "https://www.twitter.com"],
    ["linkedin", "https://www.linkedin.com"],

    # Educational Platforms
    ["college portal", "https://mrei.icloudems.com"],
    ["coursera", "https://www.coursera.org"],
    ["udemy", "https://www.udemy.com"],
    ["khan academy", "https://www.khanacademy.org"],

    # Productivity Tools
    ["google drive", "https://drive.google.com"],
    ["google docs", "https://docs.google.com"],

    # Shopping
    ["amazon", "https://www.amazon.com"],
    ["flipkart", "https://www.flipkart.com"],

    # Coding & Development
    ["github", "https://www.github.com"],
    ["geeksforgeeks", "https://www.geeksforgeeks.org"],

]


def flashthebot():   #THE MAIN PROGRAM ... !!!!!!
    wish()
    while True:

        purge()
        query = takecommand().lower()
        assisted = False

# LOGICS FOR ALL TASKS...

        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                assisted = True
                speak("Sure, here you go")
                wb.open(site[1])


        if "notepad" in query:
            assisted = True
            speak("sure")
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2410.21.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        if any(x in query for x in ["start typing", "type what I say"]):
            assisted = True
            typewrite()
        
        if "cmd" in query or "command prompt" in query:
            assisted = True
            speak("sure, lesgo catto")
            os.system("start cmd")

        #if "webcam" in query:
            #cap = cv2.VideoCapture(0)
            #while True:
                #ret, img = cap.read()
                #cv2.imshow('webcam', img)
                #k = cv2.waitKey(50)
                #if k==27:
                    #break;
            #cap.release()
            #cv2.destroyAllWindows()
        
        if "my ip" in query or "the ip" in query or " ip" in query:
            assisted = True
            ip = get('https://api.ipify.org').text
            speak(ip)

        if any(x in query for x in ["hello"]):
            assisted = True
            speak_with_random_responsepyttsx("hello")

        if any(x in query for x in ["wake up", "are you up"]):
            assisted = True
            speak_with_random_responsepyttsx("iamup")
        
        if "open whatsapp" in query:
            assisted = True
            speak("ok")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\WhatsApp.lnk"
            os.startfile(npath)
       
        if "settings" in query:
            assisted = True
            pyautogui.hotkey("win", "i")

        if "send message to" in query:
            assisted = True
            query = query.replace("send message to", "")
            person = query
            speak("what msg to send sir?")
            msg = takecommand().lower()
            if msg is not None:
                pyautogui.press("win") 
                time.sleep(1)          
                pyautogui.typewrite("whatsapp")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(1.2)
                pyautogui.typewrite(person)
                time.sleep(1.2)
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.press("enter")
                time.sleep(0.1)
                pyautogui.write(msg)
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.hotkey("alt", "f4")
                speak("done sir")
            else:
                print("speak again")
                continue


        if "chat gpt" in query:
            assisted = True
            speak("kk")
            npath = "C:\\Users\\saksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\ChatGPT.lnk"
            os.startfile(npath)

        if "open genshin" in query or "open genshin impact" in query:
            assisted = True
            npath = "C:\\Program Files\\Epic Games\\GenshinImpact\\games\\Genshin Impact game\\GenshinImpact.exe"
            os.startfile(npath)

        if any(x in query for x in ["thankyou", "thank", "crazy", "amazing"]):
            assisted = True
            speak_with_random_responsepyttsx("welcome")


        if any(x in query for x in ["search on google", "search google for", "on google"]):
            assisted = True
            speak("Sure, searching google for this?")
            query = query.replace("search", "").replace("google", "").replace("for", "").replace("on", "").replace("flash", "")
            wb.open(f"https://www.google.com/search?q={query}")

        if "anime"in query:
            assisted = True
            speak("here you go weeb")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\hianime.to.lnk"
            os.startfile(npath)

        if any(x in query for x in ["play song", "play", "play the song"]):
            assisted = True
            query = query.replace("song", "").replace("play", "").replace("the", "").replace("flash", "")
            speak(f"playing {query}")
            kit.playonyt(query)

        if any(x in query for x in ["search youtube for", "search on youtube", "show youtube results for", "show results on youtube for", "on youtube"]):
            assisted = True
            query = query.replace("search youtube for", "").replace("search on youtube", "").replace("show youtube results for", "").replace("show results on youtube for", "").replace("search", "").replace("on youtube", "").replace("for", "")
            wb.open(f"https://www.youtube.com/results?search_query={query}")

        
        if any(x in query for x in ["sleep", "exit", "rest", "quit", "standby"]):
            assisted = True
            speak_with_random_responsepyttsx("goodbye")
            break
        
        if any(x in query for x in ["shutdown", "shut down", "terminate"]):
            assisted = True
            speak("terminating kaya")
            sys.exit()
        
        if "time" in query:
            assisted = True
            strfTime = datetime.datetime.now().strftime("%H:%M")
            speak(strfTime)

        if "date" in query:
            assisted = True
            now = datetime.datetime.now()
            date_only = now.date()
            speak(date_only)

        if any(x in query for x in ["parrot", "vm", "virtual machine"]):
            assisted = True
            speak("opening the parrot v m")
            npath = "C:\\Users\\saksh\\Documents\\Virtual Machines\\parrotVM\\parrotVM.vmx"
            os.startfile(npath)

        if "joke" in query:
            assisted = True
            speak_with_random_responsepyttsx("joke")
            speak(pyjokes.get_joke())

        #if "remind me" in query:
            #speak("what should I remind you for")
            #reminder = takecommand().lower()
            #speak("after what time in minutes?")
            #minute = int(input("enter time in minutes, just the number: "))
            #seconds = minute * 60
            #set_reminder(reminder, seconds)

        if any(x in query for x in ["change my window", "change window", "change this window"]):
            assisted = True         
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            speak("this?")
            while True:
                query = takecommand().lower()
                if "no" in query or "next" in query:
                    pyautogui.press("tab")
                    speak("this?")
                if "yes" in query or "ok" in query or "this" in query or "open" in query:
                    pyautogui.keyUp("alt")
                    break

        if any(x in query for x in ["switch my window", "switch window", "switch this window"]):
            assisted = True
            pyautogui.hotkey("alt", "tab")

        if any(x in query for x in ["maximize", "full screen"]):
            assisted=True
            pyautogui.hotkey("win", "up")

        if any(x in query for x in ["minimize"]):
            assisted=True
            pyautogui.hotkey("win", "down")
            time.sleep(0.1)
            pyautogui.hotkey("win", "down")

        if "screen navigation" in query:
            assisted = True
            screen_navigation()

        if any(x in query for x in ["close this window", "close window", "close this"]):
            assisted = True
            pyautogui.hotkey("alt", "f4")

        if "stop" in query:
            assisted = True
            speak("ok")

        if "how to" in query:
            assisted = True
            query = query.replace("how to", "").replace("flash", "").replace("tell me", "")
            max_results = 1
            how_to = search_wikihow(query, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        
        if any(x in query for x in ["battery"]):
            assisted = True
            battery = psutil.sensors_battery()
            percent = battery.percent
            speak(f"we have {percent} percent battery right now")

        if any(x in query for x in ["alarm", "wake me"]):
            assisted=True
            query_for_alarm = query
            alarm_thread = threading.Thread(target=alarm, args=(query_for_alarm,))#   |_ this is alarm thread init
            alarm_thread.start() #                                                    |
        
        if any(x in query for x in ["introduce yourself", "who are you", "about you", "about yourself"]):
            assisted=True
            speak(f"Hi! I'm Flash, {mastername}'s desktop assistant. I'm designed to be fast and efficient, always ready to tackle tasks and deliver results in a flash.")
            speak("and we have another background bot named kaya, wait, lemme ask it to introduce itself real fast.")
            speak_with_gtts("hi there, i'm kaya. i handle tasks with threading and speak a bit slow, please don't mind me, talk to flash, he's better")
            speak("well, may i know your name?")
            name = takecommand().lower()
            name = name.replace("hello", "").replace("flash", "").replace("kaya", "").replace("my", "").replace("i am", "").replace("name", "").replace("is", "").replace("hi", "").replace("myself", "").replace("this is", "").replace("I'm", "").replace("i m", "").replace("there", "")
            speak(f"hi there {name}, it's a pleasure to meet you. I really wanted to have a convo with you but my lazy and dumb master doesn't know AI, shit i spoke alot, sorry sir, back to work")
        
        if any(x in query for x in ["your owner", "your master", "your sir", "created you", "made you"]):
            assisted = True
            speak("I'm programmed by my owner Saksham Jain")


        if not assisted:
            if query == None:
                print("speak again...")
            else:
                query = takecommand().lower()
                model = model_of_your_choice_on_ollama
                prompt = query

                try:
                    stream = ollama.chat(
                        model=model,
                        messages=[{'role': 'user', 'content': prompt}],
                        stream=True,
                    )

                    full_response = ""
                    current_sentence = ""  # Accumulate content for a sentence
                    for chunk in stream:
                        content = chunk.get('message', {}).get('content', '')
                        print(content, end='', flush=True)
                        full_response += content
                        current_sentence += content

                        # Check for sentence boundaries (. ! ?) and speak
                        if any(punct in current_sentence for punct in ['.', '!', '?']):
                            speak(current_sentence.strip())  # Speak the full sentence
                            current_sentence = ""  # Reset for the next sentence

                    # Speak any remaining text (if the last chunk wasn't a full sentence)
                    if current_sentence:
                        speak(current_sentence.strip())

                    print("\n")
                    print(f"Full Response: {full_response}")

                except Exception as e:
                    print(f"speak again..., error > {e}")

if __name__ == "__main__":
    while True:
        
        purge()
        permission = takecommand().lower()
        if any(x in permission for x in ["wake up", "breakup"]):
            flashthebot()
        if any(x in permission for x in ["terminate", "shut down", "shutdown", "kill system"]):
            speak("flash and kaya have been terminated for now")
            winsound.Beep(900, 500)
            purge()
            sys.exit()
