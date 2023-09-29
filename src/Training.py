
import pytesseract
from PIL import Image
import cv2
import numpy as np
import re
import logging

from src.screen_capture import capture_dark_and_darker_window

# Set up logging
logging.basicConfig(filename='ocr.log', level=logging.INFO)

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Initialize variables for drawing bounding boxes
drawing = False
start_point = (-1, -1)
end_point = (-1, -1)

# Create a copy of the image for drawing
image_copy = None


def process_ocr_result(ocr_text):
    # Implement logic to process the OCR result
    logging.info("Processed OCR Result:")
    logging.info(ocr_text)
    # Add your custom processing logic here


# Define the file to store annotated data
annotated_data_file = 'annotated_data.txt'

# Initialize an empty list to store annotated data
annotated_data = []

# Function to handle mouse events for drawing bounding boxes


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

# Function for more advanced OCR processing using regular expressions


def advanced_ocr_processing(ocr_text):
    # Define a regular expression pattern to match product names and prices
    pattern = r'\[([^\]]+)\] price (\d{4}G)'

    matches = re.findall(pattern, ocr_text)

    if matches:
        for match in matches:
            product_name, price = match
            print(f"Product Name: {product_name}, Price: {price}")

# Function to perform OCR and annotate data


def perform_ocr_and_annotation():
    global screenshot, image_copy

    # Capture the trade window region and get both the image and region
    screenshot, trade_window_region = capture_dark_and_darker_window()

    if screenshot:
        try:
            # Convert the screenshot to a format that pytesseract can process
            trade_window_image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

            # Perform OCR on the captured image
            ocr_result = pytesseract.image_to_string(trade_window_image)

            # Process the OCR result
            process_ocr_result(ocr_result)

            # Convert the image to a NumPy array for OpenCV processing
            image_np = np.array(trade_window_image)

            # Display the captured image
            cv2.imshow("Captured Image", image_np)

            # Set up the mouse callback function for drawing bounding boxes
            cv2.setMouseCallback("Captured Image", draw_bounding_box)

            # Create a copy of the image for drawing
            image_copy = np.copy(image_np)

            # Prompt the user to draw bounding boxes around text regions
            print("Draw bounding boxes around text regions and press 's' to save annotations...")
            while True:
                cv2.imshow("Captured Image", image_copy)
                key = cv2.waitKey(1)

                if key == ord('s'):
                    break

            # Extract text from the annotated image using OCR
            annotated_text = pytesseract.image_to_string(image_copy)

            # Append annotated data to the list
            annotated_data.append(annotated_text)

            # Save annotated data to the file
            with open(annotated_data_file, 'w') as file:
                for item in annotated_data:
                    file.write(f"{item}\n")

            # Close the image display window
            cv2.destroyAllWindows()
        except Exception as e:
            logging.error(f"Error processing trade window: {str(e)}")
            print(f"Error processing trade window: {str(e)}")
    else:
        print("Failed to capture the screenshot.")

# Main function


def main():
    # Perform OCR and annotation three times at the beginning
    for _ in range(3):
        perform_ocr_and_annotation()





if __name__ == "__main__":
    main()
