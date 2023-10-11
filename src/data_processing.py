import csv
import logging
import os
import re
import queue

import pytesseract

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def perform_ocr(image_path):
    """
    Perform OCR on the image specified by image_path using Tesseract.

    Parameters:
        image_path (str): The path to the image file.

    Returns:
        str: The text extracted from the image.
    """
    try:
        # Use Tesseract to do OCR on the image
        extracted_text = pytesseract.image_to_string(image_path)

        # Log the extracted text
        logging.info(f"Extracted Text: {extracted_text}")

        return extracted_text
    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred during OCR: {str(e)}")
        return None


screenshot_file_path = 'screenshot_dnd_left_half.png'
csv_file_path = 'processed_data.csv'

def read_image_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("Screenshot file does not exist.")
        return None





def process_ocr_results(data_queue, screenshot_file_path, csv_file_path):
    try:
        text = data_queue.get_nowait()
    except queue.Empty:  # Ensure queue is imported
        print("Queue is empty. No text data to process.")
        return

    image_data = read_image_data(screenshot_file_path)
    if image_data is not None:
        pattern = re.compile(r'\[(.*?)\] (.*?) : \[(.*?)\](x\d+)? (\d+g)')
        matches = pattern.findall(text)
        # ... (rest of the function)

        existing_data = []
        # Check if the file exists before trying to read it
        if os.path.exists(csv_file_path):
            try:
                # Open the file in read mode for reading
                with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    existing_data = [row for row in reader]
            except FileNotFoundError:
                logging.warning(f"File not found: {csv_file_path}. A new file will be created.")

        with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for match in matches:
                timestamp, name, item, amount, price = match

                # Validate extracted data
                if not item or not price:
                    logging.warning("Invalid data extracted. Item: %s, Price: %s", item, price)
                    continue

                # Check for duplicates
                is_duplicate = any(
                    e_item == item and e_price == price for _, _, e_item, _, e_price in existing_data
                )
                if not is_duplicate:
                    writer.writerow([timestamp, name, item, amount, price])
                    logging.info("Added new data: %s, %s, %s, %s, %s", timestamp, name, item, amount, price)


if __name__ == '__main__':
    screenshot_file_path = 'screenshot_dnd_left_half.png'
    csv_file_path = 'processed_data.csv'


    print("Current Working Directory:", os.getcwd())

    # Example usage of process_ocr_results
    extracted_text = perform_ocr(screenshot_file_path)
    if extracted_text:
        process_ocr_results(extracted_text, screenshot_file_path, csv_file_path)

