import re

def process_ocr_results(text):
    # Regular expression pattern to match the format
    pattern = r'\[(\d{2}:\d{2}:\d{2}[AM|PM]{2})\] \(([^)]+)\) : ([^:]+): (\d{4}G)'

    matches = re.findall(pattern, text)
    data_list = []
    for match in matches:
        timestamp, name, item, gold = match
        data_dict = {
            'timestamp': timestamp,
            'name': name,
            'item': item,
            'price': gold,
            'color': None  # Placeholder for color, adjust as needed
        }
        data_list.append(data_dict)
    return data_list
