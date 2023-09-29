
from src.csv_exporter import export_to_csv
from src.screen_capture import capture_screen
from src.text_extraction import extract_text_from_image
import datetime
import pygetwindow as gw
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():
    # Define the headers for the CSV

    # Get the window by its title
    window_title = 'Dark and Darker'

    # Use getWindowsWithTitles to find the window
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        # If the window is found, use the first window in the list
        window = windows[0]

        # Define the region to capture the left half of the window
        region = (window.left, window.top, window.width // 2, window.height)

        while True:
            print(window, region)
            # Capture the specified region
            screenshot = capture_screen(region)

            # Extract text from the screenshot
            text = extract_text_from_image(screenshot)
            print(text)
            # Process the extracted text
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            messages = text.splitlines()
            data = [[timestamp, message] for message in messages]

            # Export the data to a CSV file
            export_to_csv(data, "output.csv")
            print(text)


if __name__ == "__main__":
    main()
