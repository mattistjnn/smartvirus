import time
import pyautogui

# Simule la pression de la touche Windows
pyautogui.hotkey('winleft')
time.sleep(0.2)

# Écrit "Protection contre les virus et menaces" et appuie sur Entrée
pyautogui.write("Protection contre les virus et menaces")
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)

# Appuie plusieurs fois sur la touche Tab
for _ in range(4):
    pyautogui.press('tab')
    time.sleep(0.2)

# Appuie sur la touche Retour Arrière deux fois
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('space')
time.sleep(1)

# Appuie sur la touche Flèche Gauche et sur Entrée
pyautogui.press('left')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
