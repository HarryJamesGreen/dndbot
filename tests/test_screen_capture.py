
from src.screenshot_dnd import screenshot_dnd_left_half
import time

def test_screen_capture():
    screenshot, _ = screenshot_dnd_left_half()
    if screenshot:
        screenshot.save("test_screenshot.png", "PNG")
        print("Screenshot saved as test_screenshot.png")
    else:
        print("Screenshot capture failed.")
    time.sleep(2)

test_screen_capture()