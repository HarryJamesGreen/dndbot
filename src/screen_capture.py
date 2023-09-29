import pyautogui
import pygetwindow as gw


def capture_dark_and_darker_window():
    """
    Captures the content of the "Dark and Darker" window.
    :return: A PIL Image representing the captured content or None if the window is not found.
    """
    window_title = 'Dark and Darker'
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        # If the window is found, use the first window in the list
        window = windows[0]

        # Calculate the region for the bottom left tenth of the window
        tenth_width = window.width // 2
        tenth_height = window.height // 3
        region = (window.left, window.top + window.height - tenth_height, tenth_width, tenth_height)

        return pyautogui.screenshot(region=region)
    else:
        print(f"Window with title '{window_title}' not found.")
        return None
