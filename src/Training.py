import logging
import re
import cv2
import numpy as np
import queue
from PIL import Image
import pytesseract
from src.data_processing import process_ocr_results
from src.screenshot_dnd import screenshot_dnd_left_half

# Set up logging
logging.basicConfig(filename='Training.log', level=logging.INFO)

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Initialize variables for drawing bounding boxes
drawing = False
start_point = (-1, -1)
end_point = (-1, -1)

# Create a copy of the image for drawing
image_copy = None

# Define the file to store annotated data
annotated_data_file = 'Training_Data.txt'

# Initialize an empty list to store annotated data
annotated_data = []

def draw_bounding_box(event, x, y, flags, param):
    global drawing, start_point, end_point, image_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image_copy = np.copy(screenshot)
            cv2.rectangle(image_copy, start_point, (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(image_copy, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Captured Image", image_copy)

def advanced_ocr_processing(ocr_text):
    pattern = r'\[([^\]]+)\] price (\d{4}G)'
    matches = re.findall(pattern, ocr_text)

    if matches:
        for match in matches:
            product_name, price = match
            print(f"Product Name: {product_name}, Price: {price}")


def perform_ocr_and_annotation():
    global screenshot, image_copy

    print("Performing OCR annotation...")

    # Attempt to capture a screenshot
    try:
        screenshot = screenshot_dnd_left_half()
    except Exception as e:
        logging.error(f"Error capturing screenshot: {str(e)}")
        print("Error capturing screenshot. Please check the logs for more details.")
        return

    # Validate the screenshot
    if screenshot is None or screenshot.size == (0, 0):
        logging.error("Invalid screenshot obtained.")
        print("Invalid screenshot obtained. Ensure the target window is available and retry.")
        return

    try:
        trade_window_image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())
        ocr_result = pytesseract.image_to_string(trade_window_image)
        process_ocr_results(ocr_result, 'screenshot_dnd_left_half.png', 'processed_data.csv')

        image_np = np.array(trade_window_image)

        # Validate the image shape
        if image_np.shape[0] <= 0 or image_np.shape[1] <= 0:
            logging.error("Invalid image shape.")
            print("Invalid image shape. Ensure the screenshot is not empty and retry.")
            return

        cv2.imshow("Captured Image", image_np)
        cv2.setMouseCallback("Captured Image", draw_bounding_box)
        image_copy = np.copy(image_np)

        print("Draw bounding boxes around text regions and press 's' to save annotations...")

        while True:
            cv2.imshow("Captured Image", image_copy)
            key = cv2.waitKey(1)

            if key == ord('s'):
                print("Saving annotations...")
                break

    except Exception as e:
        logging.error(f"Error processing trade window: {str(e)}")
        print("Error processing trade window. Please check the logs for more details.")

def main():
    for _ in range(3):
        perform_ocr_and_annotation()

if __name__ == "__main__":
    main()
