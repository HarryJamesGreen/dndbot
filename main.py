from src.csv_exporter import export_to_csv
from src.screen_capture import capture_screen
import pygetwindow as gw
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():
    data_to_export = []

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
            screenshot.save("screenshot.png")

            # Try to extract text from the screenshot
            try:
                text = pytesseract.image_to_string(screenshot)
                time.sleep(2)
            except Exception as e:
                print(f"Error extracting text: {e}")
                continue  # Skip the current iteration and continue with the next
            print(text)
            # Append the extracted text to data_to_export
            for line in text.splitlines():
                data_to_export.append([line])

            # Export the data to the CSV file
        export_to_csv(data_to_export)


if __name__ == "__main__":
    main()
