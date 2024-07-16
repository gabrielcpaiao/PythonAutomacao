import pyautogui
import time
import pandas as pd

print(pyautogui.size())

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")


time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=685, y=451)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
time.sleep(3)
pyautogui.write("sua senha")


pyautogui.click(x=955, y=638) # clique no botao de login
