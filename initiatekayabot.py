import speech_recognition as sr
import os
import pyautogui
import time

def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    query = r.recognize_google(audio)  # Replace with your preferred recognition method
    print("Recognized:", query)
    return query.lower()
  except Exception as e:
    print("Error:", e)
    return "none"

if __name__ == "__main__":
  while True:
    query = takecommand()

    if any(x in query for x in ["wake up kaya", "wake up", "wiki wiki", "breakup kaya"]):
      os.system("start cmd")
      time.sleep(1)
      pyautogui.typewrite("python \"c:/Users/saksh/Desktop/kayathebot/kayaentry.py\"")
      time.sleep(1)
      pyautogui.press("enter")
      time.sleep(1)
      os._exit()