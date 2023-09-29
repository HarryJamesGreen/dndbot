import pyautogui

def capture_screen(region):
    """
    Captures the screen content within the specified region.
    :param region: A tuple of (x, y, width, height) representing the region to capture.
    :return: A PIL Image representing the captured content.
    """
    return pyautogui.screenshot(region=region)
