import pytesseract
import logging
from datetime import datetime
import csv

from src.csv_exporter import export_to_csv
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results

# Set up logging
logging.basicConfig(filename='docs/ocr.log', level=logging.INFO)

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Error Handling


def save_raw_ocr_to_csv(text, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])

def main():
    global last_processed_timestamp

    perform_training = input("Do you want to perform training? (yes/no): ").strip().lower()
    if perform_training == 'yes':
        for _ in range(3):
            perform_ocr_and_annotation()

    data_to_export = []

    while True:
        screenshot, region = capture_dark_and_darker_window()
        if screenshot:
            screenshot.save("screenshot.png", "PNG")
            try:
                text = pytesseract.image_to_string('screenshot.png')
                print(f"Extracted Text: {text}")
                save_raw_ocr_to_csv(text, 'docs/output.csv')
            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
                # Additional logging or actions...
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                # Additional logging or actions...

            # Debugging: Check if the function is being called
            print("Processing OCR results...")
            processed_data_list = process_ocr_results(text)


            data_to_export.extend(processed_data_list)
            export_to_csv(data_to_export, 'docs/processed_data.csv')

            processed_data_list = process_ocr_results(text)
            if processed_data_list is None:
                data_to_export.extend(processed_data_list)
            else:
                print("There is nothing to export")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()