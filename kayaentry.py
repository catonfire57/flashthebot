import os
import pyautogui
import time

password = "9354401041"
while True:
    if input("Enter password: ") == password:
        os.system("start cmd")
        time.sleep(1)
        pyautogui.typewrite("python \"c:/Users/saksh/Desktop/kayathebot/kaya.py\"")
        time.sleep(1)
        pyautogui.press("enter")
        os._exit(0)
    else:
        print("Failed Auth...:")
        print("try again...\n")