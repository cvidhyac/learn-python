# This program does not work on mac because of inherent privacy controls
# and may be it has some other blockers. Used this to explore different methods
# in the library.
#
# Especially the screenshot feature is awesome, it seems faster than getting it
# done on mac using inbuilt app.

import os
import pyautogui


def mouse_control():
    # Represents width and helight
    width, size = pyautogui.size()
    print("Width " + str(width) + "Size " + str(size))

    # current position
    current_coordinates = pyautogui.position()
    print(current_coordinates)

    # Move mouse
    pyautogui.moveTo(10, 200)

    # Move mouse for a duration of 2.5 sec
    pyautogui.move(10, 10, duration=2.5)

    # Click the mouse
    pyautogui.click()


def keyboard_control():
    pyautogui.click(100, 100)
    pyautogui.typewrite("Hello World")
    pyautogui.press("F1")
    pyautogui.hotkey()
    print("Execution complete!")


# Take a screenshot and save to current directory
def screenshot_features():
    pyautogui.screenshot(os.getcwd() + "/resources/screenshot.png")


mouse_control()
keyboard_control()
screenshot_features()
