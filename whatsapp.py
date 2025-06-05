import pyautogui
import time

mesaj =""

mesaj_sayisi=100
for _ in range(mesaj_sayisi):
    pyautogui.typewrite(mesaj)
    pyautogui.press("enter")
    time.sleep(1)

