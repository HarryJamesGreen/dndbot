import numpy as np
import pytesseract
import time
import logging
from datetime import datetime
import csv

from src.csv_exporter import export_to_csv
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results
from src.text_extraction import extract_text_and_color_from_image

# Set up logging
logging.basicConfig(filename='../docs/ocr.log', level=logging.INFO)
# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Initialize variables for the last processed timestamp
last_processed_timestamp = datetime(1900, 1, 1)  # Initialize with a very old timestamp

def save_raw_ocr_to_csv(text, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])

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
            # Convert the PIL Image to a numpy array
            screenshot_np = np.array(screenshot)
            # Try to extract text from the screenshot
            try:
                text, color = extract_text_and_color_from_image(screenshot_np)
                print(f"Extracted Text: {text} | Extracted Color: {color}")
                # Save the raw OCR text to output.csv
                save_raw_ocr_to_csv(text, 'docs/output.csv')
            except Exception as e:
                print(f"Error extracting text: {e}")
                continue  # Skip the current iteration and continue with the next
            print(text)
            # Save the screenshot as a JPEG as a workaround for the PIL error
            screenshot.save("screenshot.jpg", "JPEG")
        else:
            print("Failed to capture the screenshot.")
            continue

        # Process the OCR results and get the processed data
        processed_data = {
            'timestamp': ...,
            'name': ...,
            'item': text,
            'price': ...,
            'color': color
        }

        # Update the last processed timestamp to the latest timestamp in the processed data
        if processed_data and isinstance(processed_data, dict) and 'timestamp' in processed_data:
            last_processed_timestamp = processed_data['timestamp']

        # Append the processed data to data_to_export
        data_to_export.append(processed_data)

        # Export the data to the CSV file
        export_to_csv(data_to_export, 'docs/processed_data.csv')

if __name__ == "__main__":
    main()
