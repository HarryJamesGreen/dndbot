from src.screen_capture import capture_screen
from src.text_extraction import extract_text_from_image
from src.csv_exporter import export_to_csv
import pytesseract
import datetime
import pygetwindow as gw
import time
import pyautogui
import random
from src.mouse_interaction import jiggle_mouse

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Adjust the path accordingly

def main():
    # Define the headers for the CSV
    headers = ['Timestamp', 'Message']

    # Get the window by its title
    window_title = 'Dark and Darker'
    window = gw.getWindowsWithTitle(window_title)[0]

    # Define the region to capture the left half of the window
    region = (window.left, window.top, 640, 720)

    while True:
        # Capture the specified region
        screenshot = capture_screen(region)

        # Extract text from the screenshot
        text = extract_text_from_image(screenshot)

        # Process the extracted text
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messages = text.splitlines()
        data = [[timestamp, message] for message in messages]

        # Export the data to a CSV file
        export_to_csv(data, headers)


if __name__ == "__main__":
    main()
