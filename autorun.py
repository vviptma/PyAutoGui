#AUTO RUN
import keyboard
import pyautogui
import pydirectinput
while True:
    if keyboard.is_pressed("q"):
        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('w')
        pyautogui.alert('STOP')
        break
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('w')