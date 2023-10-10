import pytesseract
import logging
import csv
from tqdm import tqdm
import time
import keyboard  # Import the keyboard library
from src.csv_exporter import export_to_csv
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results
import subprocess  # Import subprocess module

# Path to the LibreOffice Calc executable
libreoffice_executable = "C:\Program Files\LibreOffice\program\sscalc.exe"
# Path to your spreadsheet file
spreadsheet_file = "C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\docs\processed_data.csv"

# Configure logging
logging.basicConfig(filename='docs/ocr.log', level=logging.INFO)

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def save_raw_ocr_to_csv(text, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])


def main():
    print("Welcome to the sniping tool")
    perform_training = input('Do you want to perform training? (yes/no): ').strip().lower()

    if perform_training == 'yes':
        print("Performing OCR and Annotation...")
        for _ in tqdm(range(3), desc="Performing OCR and Annotation", ascii=False, ncols=75):
            perform_ocr_and_annotation()
            time.sleep(0.01)  # Simulating a delay

    print("Press [Esc] at any time to exit the program.")
    data_to_export = []

    # Open LibreOffice Calc with the CSV file
    subprocess.Popen([libreoffice_executable, spreadsheet_file])

    while True:
        # Check if 'Esc' is pressed
        if keyboard.is_pressed('Esc'):
            print("Exiting the program...")
            break

        screenshot, region = capture_dark_and_darker_window()
        if screenshot:
            screenshot.save("screenshot.png", "PNG")
            try:
                text = pytesseract.image_to_string('screenshot.png')
                logging.info(f"Extracted Text: {text}")

                # Save raw OCR output to CSV
                save_raw_ocr_to_csv(text, 'docs/output.csv')

            except UnicodeDecodeError as e:
                logging.error(f"UnicodeDecodeError: {e}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")

            # Process OCR results with a progress bar
            print("Processing OCR results...")
            for _ in tqdm(range(100), desc="Processing OCR results", ascii=False, ncols=75):
                processed_data_list = process_ocr_results(text)
                time.sleep(0.01)  # Simulating a delay

            if processed_data_list is not None:
                data_to_export.extend(processed_data_list)
                export_to_csv(data_to_export, 'docs/processed_data.csv')
            else:
                logging.warning("There is nothing to export")


if __name__ == '__main__':
    main()
