import re


def process_ocr_results(text):
    # Regular expression pattern to match the format
    pattern = r'\[(\d{2}:\d{2}:\d{2}[AM|PM]{2})\] \(([^)]+)\) : ([^:]+): (\d{4}G)'

    matches = re.findall(pattern, text)
    for match in matches:
        timestamp, name, item, gold = match
        # Process the extracted data as needed
        print(f"Timestamp: {timestamp}, Name: {name}, Item: {item}, Gold: {gold}")