#LIBRARY
import keyboard
import pyautogui
import pydirectinput

#LOOP
soluong = 1
while True:
    if keyboard.is_pressed("q"):
        pyautogui.alert('STOP ALL')
        break
    #STOP
    print('--------BẮT ĐẦU--------')
    if(soluong >21):
        print('--------ĐÃ ĐỦ SỐ LƯỢNG--------')
        pyautogui.alert('ĐÃ ĐỦ SỐ LƯỢNG')
        break
    elif (pyautogui.locateCenterOnScreen('phim1.png') is not None):
        pydirectinput.press('1')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím 1')
        continue
    elif (pyautogui.locateCenterOnScreen('phim2.png') is not None):
        pydirectinput.press('2')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím 2')
        continue
    elif (pyautogui.locateCenterOnScreen('phim3.png') is not None):
        pydirectinput.press('3')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím 3')
        continue
    elif (pyautogui.locateCenterOnScreen('phim4.png') is not None):
        pydirectinput.press('4')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím 4')
        continue
    elif (pyautogui.locateCenterOnScreen('phim5.png') is not None):
        pydirectinput.press('5')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím 5')
        continue
    elif (pyautogui.locateCenterOnScreen('phimC.png') is not None):
        pydirectinput.press('c')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím C')
        continue
    elif (pyautogui.locateCenterOnScreen('phimE.png') is not None):
        pydirectinput.press('e')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím E')
        continue
    elif (pyautogui.locateCenterOnScreen('phimH.png') is not None):
        pydirectinput.press('h')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím H')
        continue
    elif (pyautogui.locateCenterOnScreen('phimG.png') is not None):
        pydirectinput.press('g')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím G')
        continue
    elif (pyautogui.locateCenterOnScreen('phimZ.png') is not None):
        pydirectinput.press('z')
        print('Số lượng:'+soluong)
        soluong = soluong + 1
        print('phím Z')
        continue
    print('--------KẾT THÚC--------')