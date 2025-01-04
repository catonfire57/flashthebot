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

pygame.init()
pygame.mixer.init()

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('rate', 200)
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
thread_batterycheck = threading.Thread(target=batterycheck) #                          _____
thread_batterycheck.daemon = True # Allow program to exit even if thread is running        |
thread_batterycheck.start() #                                                              |   HERE WE INIT THE THREAD FOR BATTERYCHECK IN BG!!
#                                                                                       ___|  

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
    "hello": ["hello sir, I'm up", "Hi sir, what can I do for you", "I'm right here, ready to help"],
    "iamup": ["I'm up and working fine", "I can't sleep without your permission hence I'm up", "I don't remember you asking me to sleep"]
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
    ["movie", "https://vipstream.com"],

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

# ALL TASKS LOGIC

        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                speak("Sure, here you go")
                wb.open(site[1])
                assisted = True


        if "notepad" in query:
            speak("sure")
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2410.21.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)
            assisted = True

        if any(x in query for x in ["start typing", "type what I say"]):
            typewrite()
            assisted = True
        
        if "cmd" in query or "command prompt" in query:
            speak("sure, lesgo catto")
            os.system("start cmd")
            assisted = True

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
        
        if "my ip" in query or "the ip" in query:
            ip = get('https://api.ipify.org').text
            speak(ip)
            assisted = True

        if any(x in query for x in ["hello"]):
            speak_with_random_responsepyttsx("hello")
            assisted = True

        if any(x in query for x in ["wake up", "are you up"]):
            speak_with_random_responsepyttsx("iamup")
            assisted=True
        
        if "open whatsapp" in query:
            speak("ok")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\WhatsApp.lnk"
            os.startfile(npath)
            assisted = True
       
        if "settings" in query:
            pyautogui.hotkey("win", "i")
            assisted = True

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
            speak("kk")
            npath = "C:\\Users\\saksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\ChatGPT.lnk"
            os.startfile(npath)
            assisted = True

        if "open genshin" in query or "open genshin impact" in query:
            npath = "C:\\Program Files\\Epic Games\\GenshinImpact\\games\\Genshin Impact game\\GenshinImpact.exe"
            os.startfile(npath)
            assisted = True

        if any(x in query for x in ["thankyou", "thank", "crazy", "amazing"]):
            speak_with_random_responsepyttsx("welcome")
            assisted = True


        if any(x in query for x in ["search on google", "search google for", "on google"]):
            speak("Sure, searching google for this?")
            query = query.replace("search", "").replace("google", "").replace("for", "").replace("on", "").replace("flash", "")
            wb.open(f"https://www.google.com/search?q={query}")
            assisted = True

        if "anime"in query:
            speak("here you go weeb")
            npath = "C:\\Users\\saksh\\Desktop\\flashthebot\\Shortcuts ( dont delete )\\hianime.to.lnk"
            os.startfile(npath)
            assisted = True

        if any(x in query for x in ["play song", "play", "play the song"]):
            query = query.replace("song", "").replace("play", "").replace("the", "").replace("flash", "")
            speak(f"playing {query}")
            kit.playonyt(query)
            assisted= True

        if any(x in query for x in ["search youtube for", "search on youtube", "show youtube results for", "show results on youtube for", "on youtube"]):
            query = query.replace("search youtube for", "").replace("search on youtube", "").replace("show youtube results for", "").replace("show results on youtube for", "").replace("search", "").replace("on youtube", "").replace("for", "")
            wb.open(f"https://www.youtube.com/results?search_query={query}")
            assisted = True

        
        if any(x in query for x in ["sleep", "exit", "rest", "quit", "shut down", "shutdown", "standby"]):
            speak_with_random_responsepyttsx("goodbye")
            assisted = True
            break
        
        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            speak(strfTime)
            assisted = True

        if "date" in query:
            now = datetime.datetime.now()
            date_only = now.date()
            speak(date_only)
            assisted = True

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
            pyautogui.hotkey("alt", "tab")
            assisted = True

        if "screen navigation" in query:
            assisted = True
            screen_navigation()

        if any(x in query for x in ["close this window", "close window", "close this"]):
            assisted = True
            pyautogui.hotkey("alt", "f4")

        #if not assisted:
            #speak("Sorry, I can't assist you with that, but I'm still learning")

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
            query_for_alarm = query
            alarm_thread = threading.Thread(target=alarm, args=(query_for_alarm,))#   |_ this is alarm thread init
            alarm_thread.start() #                                                    |

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
