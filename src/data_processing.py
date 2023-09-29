import re


def process_ocr_results(text):
    # Split the text by newline
    lines = text.split('\n')

    # Define a pattern for extracting data
    # This is a basic pattern and might need adjustments based on the actual text format
    pattern = r"\[(?P<timestamp>.*?)\] (?P<name>.*?) : \[(?P<item>.*?)\] (?P<price>\d+g?)"

    processed_data = []

    for line in lines:
        match = re.search(pattern, line)
        if match:
            data = {
                'timestamp': match.group('timestamp'),
                'name': match.group('name'),
                'item': match.group('item'),
                'price': match.group('price'),
            }
            processed_data.append(data)
        else:
            print(f"Failed to process line: {line}")  # Logging the failed line for debugging

    return processed_data
