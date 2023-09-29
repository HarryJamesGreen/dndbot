import pygetwindow as gw
from src.screen_capture import capture_screen
from src.ocr_handler import extract_text_from_image  # Import from ocr_handler
from src.csv_exporter import export_to_csv
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def main():
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
            # Capture the specified region
            screenshot = capture_screen(region)

            # Extract text from the screenshot
            text = extract_text_from_image(screenshot)

            # Process the extracted text
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            messages = text.splitlines()
            data = [[timestamp, message] for message in messages]

            # Export the data to a CSV file
            export_to_csv(data, "output.csv")
            print(text)

if __name__ == "__main__":
    main()
