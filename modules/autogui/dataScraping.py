# This program will scrape indicator data from MT4 and return it to an excel spreadsheet

import pyautogui

pyautogui.FAILSAFE = True #Move mouse to upper left during testing to abort program

pyautogui.size() #For screen size reference [My size : Size(width=2736, height=1824)]
# pyautogui.position() #Use this to determine start and end position
# My start position : Point(x=2640, y=947)
# My end position: Point(x=276, y=947)
# width, height = pyautogui.size()
pyautogui.click(x=1142, y=1771, interval=1) # Position of Excel Taskbar Icon
pyautogui.click(x=1212, y=1775, interval=1) # Position of MT4 Taskbar Icon
pyautogui.moveTo(276, 947, duration=1) #Change these parameters to reflect actual starting position
xDistance, yDistance = pyautogui.position()

while xDistance < 2640:

    print(pyautogui.position())
    xDistance, yDistance = pyautogui.position()
    pyautogui.hotkey('ctrl', 'c') # Copy output from MT4
    pyautogui.hotkey('alt', 'tab') # Switch to Excel
    pyautogui.hotkey('ctrl', 'v') # Paste output to excel from MT4
    pyautogui.typewrite(['right', 'right'], interval=0.5) # goes to next empty array
    pyautogui.hotkey('alt', 'tab') # Switch back to MT4
    pyautogui.moveRel(7, 0, duration=1) # positive for date ascending, negative for date descending



