import pygetwindow as gw
import pyautogui

def capture_dark_and_darker_window():
    """
    Captures the content of the "Dark and Darker" window.
    :return: A PIL Image representing the captured content and the region coordinates, or None if the window is not found.
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

        # Capture the content and return both the captured image and the region coordinates
        captured_image = pyautogui.screenshot(region=region)
        return captured_image, region
    else:
        print(f"Window with title '{window_title}' not found.")
        return None, None  # Return None for both the image and region

# Example usage
captured_image, region = capture_dark_and_darker_window()
if captured_image:
    captured_image.save("captured_dark_and_darker.png")  # Save the captured image to a file

# Now you can use the 'region' variable in your other script (Training.py)
