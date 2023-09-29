import pyautogui
import pygetwindow as gw

def capture_specific_window(title):
    window = gw.getWindowsWithTitle(title)[0]
    left, top, width, height = window.left, window.top, window.width, window.height
    return pyautogui.screenshot(region=(left, top, width, height))
