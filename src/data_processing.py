import re
import csv
import logging
import os


def read_image_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("Screenshot file does not exist.")
        return None


def process_ocr_results(text, screenshot_file_path, csv_file_path):
    image_data = read_image_data(screenshot_file_path)

    if image_data is not None:
        pattern = re.compile(r'\[(.*?)\] (.*?) : \[(.*?)\](x\d+)? (\d+g)')
        matches = pattern.findall(text)

        existing_data = []
        try:
            with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
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
    screenshot_file_path = 'screenshot.png'
    csv_file_path = os.path.join(os.getcwd(), 'docs', 'processed_data.csv')

    print("Current Working Directory:", os.getcwd())

    # Example usage:
    text = "Your OCR text here"  # Replace with your actual OCR text
    process_ocr_results(text, screenshot_file_path, csv_file_path)
