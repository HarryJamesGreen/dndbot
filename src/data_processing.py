import csv
import re
from datetime import datetime


def extract_timestamp_and_text(line, timestamp_pattern):
    timestamp_match = re.search(timestamp_pattern, line)
    if not timestamp_match:
        return None, None
    timestamp_str = timestamp_match.group(0)
    text = line[len(timestamp_str):].strip()
    return timestamp_str, text


def process_line(line, timestamp_pattern):
    timestamp_str, text = extract_timestamp_and_text(line, timestamp_pattern)
    if not timestamp_str:
        return None

    parts = text.split(':')
    if len(parts) != 2:
        return None

    name, item_price = parts
    item_price_parts = item_price.split(']')
    if len(item_price_parts) != 2:
        return None

    item = item_price_parts[0].strip() + ']'
    price = item_price_parts[1].strip()
    return {
        'timestamp': datetime.strptime(timestamp_str, '[%I:%M:%S %p]'),
        'name': name.strip(),
        'item': item,
        'price': price
    }


# This approach ensures that even if multiple entries are
# posted within the same second, all of them will be captured as
# long as their combination of timestamp, name, and item is unique.
def process_ocr_results(ocr_text):
    processed_data = []
    unique_identifiers = set()
    timestamp_pattern = r'\[\d{1,2}:\d{2}:\d{2} [APap][Mm]\]'
    lines = ocr_text.split('\n')

    for line in lines:
        data = process_line(line, timestamp_pattern)  # Pass None for the last_processed_timestamp
        if data:
            # Create a unique identifier using timestamp, name, and item
            identifier = f"{data['timestamp']}_{data['name']}_{data['item']}"
            if identifier not in unique_identifiers:
                unique_identifiers.add(identifier)
                processed_data.append(data)

    return processed_data


def export_to_csv(data, csv_filename):
    try:
        with open(csv_filename, mode='w', newline='') as file:
            fieldnames = ['timestamp', 'name', 'item', 'price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f"Error exporting to CSV: {e}")


if __name__ == "__main__":
    try:
        with open('output.csv', 'r', ) as ocr_file:
            ocr_text = ocr_file.read()
        last_processed_timestamp = datetime(1900, 1, 1)
        processed_data = process_ocr_results(ocr_text, last_processed_timestamp)
        if processed_data:
            last_processed_timestamp = max(processed_data, key=lambda x: x['timestamp'])['timestamp']
        export_to_csv(processed_data, 'processed_data.csv')
    except Exception as e:
        print(f"Error in main execution: {e}")
