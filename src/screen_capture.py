import pyautogui
import pygetwindow as gw


def capture_screen(title=None, region=None):
    """
    Captures the screen, a region of the screen, or a specific window.

    Parameters:
    - title (str): Title of the window to capture. If provided, region is ignored.
    - region (tuple): (x, y, width, height) of the region to capture. Captures full screen if None.

    Returns:
    - Image: Captured screenshot.
    """
    if title:
        window = gw.getWindowsWithTitle(title)[0]
        left, top, width, height = window.left, window.top, window.width, window.height
        return pyautogui.screenshot(region=(left, top, width, height))
    else:
        return pyautogui.screenshot(region=region)