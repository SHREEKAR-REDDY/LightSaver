import pyautogui
import time

print("HODOR is keeping the screen alive. It won't let it die.  🧑‍⚕️")
while True:
    x, y = pyautogui.position()  # Get the current mouse position
    pyautogui.moveTo(x + 1, y + 1)  # Move the mouse to a new position
    time.sleep(10)  # Wait for 10 seconds
    pyautogui.moveTo(x, y)  # Move the mouse back to the original position
    time.sleep(10)  # Wait for 10 seconds