
from main import capture_dark_and_darker_window
import time

def test_screen_capture():
    screenshot, _ = capture_dark_and_darker_window()
    if screenshot:
        screenshot.save("test_screenshot.png", "PNG")
        print("Screenshot saved as test_screenshot.png")
    else:
        print("Screenshot capture failed.")
    time.sleep(2)

test_screen_capture()