import pyautogui
import time
n=int(input('Сколько заспамить вкладок'))
pyautogui.moveTo(300,1055)
pyautogui.click()
pyautogui.click()
pyautogui.moveTo(300,955)
time.sleep(1)
pyautogui.click()
for x in range(n+1):
    
    pyautogui.hotkey('ctrl','t')
    
    
    