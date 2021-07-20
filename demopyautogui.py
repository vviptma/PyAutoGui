#LIBRARY
import keyboard
import pyautogui
import pydirectinput

#LOOP
while True:
    if keyboard.is_pressed("q"):
        pyautogui.alert('STOP ALL')
        break
    #STOP
    if (pyautogui.locateCenterOnScreen('phim1.png') is not None):
        pydirectinput.press('1')
        continue
    elif (pyautogui.locateCenterOnScreen('phim2.png') is not None):
        pydirectinput.press('2')
        continue
    elif (pyautogui.locateCenterOnScreen('phim3.png') is not None):
        pydirectinput.press('3')
        continue
    elif (pyautogui.locateCenterOnScreen('phim4.png') is not None):
        pydirectinput.press('4')
        continue
    elif (pyautogui.locateCenterOnScreen('phim5.png') is not None):
        pydirectinput.press('5')
        continue
    elif (pyautogui.locateCenterOnScreen('phimC.png') is not None):
        pydirectinput.press('c')
        continue
    elif (pyautogui.locateCenterOnScreen('phimE.png') is not None):
        pydirectinput.press('e')
        continue
    elif (pyautogui.locateCenterOnScreen('phimH.png') is not None):
        pydirectinput.press('h')
        continue
    elif (pyautogui.locateCenterOnScreen('phimG.png') is not None):
        pydirectinput.press('g')
        continue
    elif (pyautogui.locateCenterOnScreen('phimZ.png') is not None):
        pydirectinput.press('z')
        continue