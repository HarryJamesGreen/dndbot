import pygetwindow as gw
from PIL import ImageGrab

def capture_dark_and_darker_window():
    # Get the window titled 'Dark and Darker'
    window = None
    for win in gw.getWindowsWithTitle(''):
        if 'dark and darker' in win.title.lower():
            window = win
            break

    if not window:
        return None

    # Capture the entire window
    screenshot = ImageGrab.grab(bbox=(window.left, window.top, window.right, window.bottom))

    # Crop to the left half of the window
    width, height = screenshot.size
    left_half = screenshot.crop((0, 0, width // 2, height))

    return left_half