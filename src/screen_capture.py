import pyautogui

def capture_screen(region=None):
    """
    Captures the screen or a region of the screen.
    
    Parameters:
    - region (tuple): (x, y, width, height) of the region to capture. Captures full screen if None.
    
    Returns:
    - Image: Captured screenshot.
    """
    screenshot = pyautogui.screenshot(region=region)
    return screenshot
