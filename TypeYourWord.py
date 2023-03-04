import pyautogui as py
import time

word = str(input("Enter your word:\n"))
print("Wait 5 seconds")
time.sleep(5)
py.typewrite(str(word))
