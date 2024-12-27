import pyttsx3
import speech_recognition as sr
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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('voices', voices[0].id)

# text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("RECOGNIZING...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("ahan?")
        return ""
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning sir, kaya is up")
    elif hour>=12 and hour<16:
        speak("good afternoon sir, kaya is up")
    else: speak("good evening sir, kaya is up")

#def set_reminder(reminder, seconds):
    #def reminder_thread():
        #speak(f"Setting a reminder for {reminder} in {seconds} seconds.")
        #time.sleep(seconds)
        #speak(f"Reminder: {reminder}")

    #thread = threading.Thread(target=reminder_thread)
    #thread.start()

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


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

# ALL TASKS LOGIC

        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                speak("Sure, here you go")
                wb.open(site[1])


        if "notepad" in query:
            speak("sure")
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2410.21.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        if any(x in query for x in ["start typing", "type what I say"]):
            typewrite()
        
        if "cmd" in query or "command prompt" in query:
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
        
        if "ip" in query:
            ip = get('https://api.ipify.org').text
            speak(ip)

        if any(x in query for x in ["hello kaya", "kaya you up", "alive", "wake up"]):
            speak("hello sir, I'm up and working fine")

        

        if "open whatsapp" in query:
            speak("sure, opening whatsapp")
            npath = "C:\\Users\\saksh\\Desktop\\Shortcuts ( dont delete )\\WhatsApp.lnk"
            os.startfile(npath)
       
        if "settings" in query:
            pyautogui.hotkey("win", "i")

        if "send message to" in query:
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
                time.sleep(1)
                pyautogui.typewrite(person)
                time.sleep(1)
                pyautogui.press("tab")
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.typewrite(msg)
                pyautogui.press("enter")
                speak("message sent sir")
                pyautogui.hotkey("alt", "f4")
            else:
                print("speak again")
                continue
        else:
            speak("I can't assist with that yet, but I'm learning!")
            continue


        if "chat gpt" in query:
            speak("kk")
            npath = "C:\\Users\\saksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\ChatGPT.lnk"
            os.startfile(npath)

        if "open genshin" in query or "open genshin impact" in query:
            npath = "C:\\Program Files\\Epic Games\\GenshinImpact\\games\\Genshin Impact game\\GenshinImpact.exe"
            os.startfile(npath)

        if "thank" in query:
            speak("my pleasure master")


        if "search on google" in query or "search google for" in query:
            speak("Sure, searching google for this?")
            query = query.replace("search", "").replace("google", "").replace("for", "").replace("on", "")
            wb.open(f"https://www.google.com/search?q={query}")

        if "anime"in query:
            speak("here you go weeb")
            npath = "C:\\Users\\saksh\\Desktop\\Shortcuts ( dont delete )\\hianime.to.lnk"
            os.startfile(npath)

        if "song" in query:
            speak("sure, what song to play?, maestro")
            song = takecommand().lower()
            kit.playonyt(song)

        
        if any(x in query for x in ["sleep", "exit", "rest", "quit"]):
            speak("goodbye sir, see you soon")
            winsound.Beep(900, 500)
            sys.exit()
        
        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            speak(strfTime)

        if "date" in query:
            now = datetime.datetime.now()
            date_only = now.date()
            speak(date_only)

        if any(x in query for x in ["parrot", "vm", "virtual machine"]):
            speak("opening the parrot v m")
            npath = "C:\\Users\\saksh\\Documents\\Virtual Machines\\parrotVM\\parrotVM.vmx"
            os.startfile(npath)

        if "joke" in query:
            speak(pyjokes.get_joke())

        #if "remind me" in query:
            #speak("what should I remind you for")
            #reminder = takecommand().lower()
            #speak("after what time in minutes?")
            #minute = int(input("enter time in minutes, just the number: "))
            #seconds = minute * 60
            #set_reminder(reminder, seconds)

        if "switch window" in query or "change window" in query:            
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

        if "screen navigation" in query:
            screen_navigation() 

        if any(x in query for x in ["close this window", "close window", "close this"]):
            pyautogui.hotkey("alt", "f4")