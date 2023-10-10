import re
import csv
import logging
import os

print("Current Working Directory:", os.getcwd())


# Regular expression to extract timestamp, username, and message
def process_ocr_results(text):

    pattern = re.compile(r'\[(.*?)\] (.*?) : \[(.*?)\](x\d+)? (\d+g)')

    matches = pattern.findall(text)

    existing_data = []
    try:
        with open('C:/Users/coolb/Desktop/New folder (2)/uni/main/Python/Python bot/docs/processed_data.csv', 'a',
                  newline='', encoding='utf-8') as file:

            reader = csv.reader(file)
            existing_data = [row for row in reader]
    except FileNotFoundError:
        logging.warning("File not found: processed_data.csv. A new file will be created.")

    with open('C:/Users/coolb/Desktop/New folder (2)/uni/main/Python/Python bot/docs/processed_data.csv', 'a',
              newline='', encoding='utf-8') as file:

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

                # Example usage
                text = "[7:26:38 AM] cheppy : [Gold Ore]x3 600g"
                ans = process_ocr_results(text)
                print(ans)