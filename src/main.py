import csv
import pytesseract
import time
import logging
from datetime import datetime

from src.csv_exporter import export_to_csv
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results

# Set up logging
logging.basicConfig(filename='ocr.log', level=logging.INFO)
# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Initialize variables for the last processed timestamp
last_processed_timestamp = datetime(1900, 1, 1)  # Initialize with a very old timestamp

def main():
    global last_processed_timestamp  # Declare last_processed_timestamp as global

    # Ask the user if they want to perform training
    perform_training = input("Do you want to perform training? (yes/no): ").strip().lower()
    if perform_training == 'yes':
        # Perform OCR and annotation three times at the beginning
        for _ in range(3):
            perform_ocr_and_annotation()

    data_to_export = []

    while True:
        # Capture the specified region
        screenshot, region = capture_dark_and_darker_window()  # Capture both the image and region
        if screenshot:
            screenshot.save("screenshot.jpeg")
        else:
            print("Failed to capture the screenshot.")

        # Try to extract text from the screenshot
        try:
            text = pytesseract.image_to_string(screenshot)
        except Exception as e:
            print(f"Error extracting text: {e}")
            continue  # Skip the current iteration and continue with the next
        print(text)

        # Process the OCR results and get the processed data
        processed_data = process_ocr_results(text)

        # Update the last processed timestamp to the latest timestamp in the processed data
        if processed_data:
            last_processed_timestamp = max(processed_data, key=lambda x: x['timestamp'])['timestamp']

        # Append the processed data to data_to_export
        data_to_export.extend(processed_data)

        # Export the data to the CSV file
        export_to_csv(data_to_export, '../processed_data.csv')

if __name__ == "__main__":
    main()