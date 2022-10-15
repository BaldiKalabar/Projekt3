import pyautogui
import time
n=int(input('Сколько заспамить -места'))

pyautogui.moveTo(150,1055)
pyautogui.click()
pyautogui.moveTo(150,955)
pyautogui.click()

time.sleep(1)
for x in range(n+1):
    pyautogui.click()
    pyautogui.hotkey('ctrl','n')
