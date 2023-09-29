import csv
import re
from datetime import datetime

import csv
import re
from datetime import datetime

def process_ocr_results(ocr_text, last_processed_timestamp):
    processed_data = []

    # Define a regex pattern for valid timestamps
    timestamp_pattern = r'\[\d{1,2}:\d{2}:\d{2} [APap][Mm]\]'

    # Split the OCR text into lines
    lines = ocr_text.split('\n')

    for line in lines:
        # Extract the timestamp and text from each line using the new pattern
        timestamp_match = re.search(timestamp_pattern, line)
        if timestamp_match:
            timestamp_str = timestamp_match.group(0)
            text = line[len(timestamp_str):].strip()

            # Convert the timestamp string to a datetime object
            timestamp = datetime.strptime(timestamp_str, '[%I:%M:%S %p]')

            # Check if the timestamp is newer than the last processed timestamp
            if timestamp > last_processed_timestamp:
                # Process the text to extract relevant information (name, item, price, etc.)
                # Here, we assume a simple format: [Name]Item Price
                parts = text.split(':')
                if len(parts) == 2:
                    name, item_price = parts
                    name = name.strip()
                    item_price = item_price.strip()

                    # Split item and price
                    item_price_parts = item_price.split(']')
                    if len(item_price_parts) == 2:
                        item = item_price_parts[0].strip() + ']'
                        price = item_price_parts[1].strip()

                        # Append the processed data to the list
                        processed_data.append({
                            'timestamp': timestamp,
                            'name': name,
                            'item': item,
                            'price': price
                        })

    return processed_data


def export_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ['timestamp', 'name', 'item', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # Read OCR text from the 'output.csv' file
    with open('output.csv', 'r',) as ocr_file:
        ocr_text = ocr_file.read()

    # Define the last processed timestamp (initialize with a very old timestamp)
    last_processed_timestamp = datetime(1900, 1, 1)

    # Process the OCR results
    processed_data = process_ocr_results(ocr_text, last_processed_timestamp)

    # Update the last processed timestamp to the latest timestamp in the processed data
    if processed_data:
        last_processed_timestamp = max(processed_data, key=lambda x: x['timestamp'])['timestamp']

    # Export the processed data to a CSV file using your original export_to_csv function
    export_to_csv(processed_data, 'processed_data.csv')
