from PIL import ImageGrab
import logging
import traceback

from PIL import Image
from PIL import ImageGrab


def screenshot_dnd_left_half():
    try:
        # Define the dimensions of the "Dark and Darker" window
        window_width = 1280
        window_height = 720

        # Calculate the dimensions for capturing the left half of the window
        capture_width = window_width // 2
        capture_height = window_height

        # Define the coordinates for capturing the left half of the window
        capture_x = 0
        capture_y = 0
        sleep_time = 10

        # Capture the left half of the window
        screenshot = ImageGrab.grab(bbox=(capture_x, capture_y, capture_x + capture_width, capture_y + capture_height))

        # Save the screenshot as an image file
        screenshot.save("screenshot_dnd_left_half.png", "PNG")
        print("Screenshot saved.")
        return screenshot  # Return the screenshot image
    except Exception as e:
        logging.error(f"An error occurred during screenshot capture: {str(e)}")
        logging.error("Traceback: ")
        logging.error(traceback.format_exc())  # Log the full traceback
        return None  # Return None if an error occurred


def open_captured_image():
    try:
        img = Image.open('screenshot_dnd_left_half.png')  # Use the correct file name
        img.show()
    except FileNotFoundError:
        print("The captured image file was not found.")
