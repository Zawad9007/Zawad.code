import time
import pyautogui
# import webbrowser

# url='https://www.messenger.com/t/100039062120038 '
# webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)

for i in range(50):
# writng the massege  
    time.sleep(1)
    pyautogui.write("Zawad is best")
    time.sleep(2)
    pyautogui.press('space')
# sending
time.sleep(10)
pyautogui.press('enter')