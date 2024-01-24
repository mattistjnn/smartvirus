import time
import pyautogui

# Simule la pression de la touche Windows + R
pyautogui.hotkey('winleft', 'r')
time.sleep(0.5)

# Écrit "shell:startup" et appuie sur Entrée
pyautogui.write("shell\:startup")
pyautogui.press('enter')
time.sleep(0.5)

# Appuie sur les touches fléchées bas et haut, puis sur Entrée
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(0.5)

# Appuie sur les touches fléchées bas et Ctrl + C
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Appuie plusieurs fois sur la touche Tab
for _ in range(5):
    pyautogui.press('tab')

# Appuie sur Ctrl + V
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
