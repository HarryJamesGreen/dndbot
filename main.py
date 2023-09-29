from src.screen_capture import capture_screen
from src.text_extraction import extract_text_from_image
from src.csv_exporter import export_to_csv
import pytesseract
import datetime
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Adjust the path accordingly

def main():
    headers = ['Timestamp', 'Message']
    while True:
        # Define the region to capture (adjust these values as needed)
        region = (100, 100, 300, 300)

        # Capture the screen region
        screenshot = capture_screen(region=region)

        # Extract text from the screenshot
        text = extract_text_from_image(screenshot)

        # Process the extracted text
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messages = text.splitlines()
        data = [[timestamp, message] for message in messages]

        # Export the data to a CSV file
        export_to_csv(data, headers)

        # Wait for a few seconds before capturing again
        time.sleep(5)  # Adjust the interval as needed

if __name__ == "__main__":
    main()
