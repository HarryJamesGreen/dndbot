import pyautogui
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Define the region of interest (ROI) for the trade window
trade_window_region = (x, y, width, height)

# Define the file to store annotated data
annotated_data_file = 'annotated_data.txt'

# Initialize an empty list to store annotated data
annotated_data = []


# Function to capture the trade window and perform OCR
def capture_trade_window_and_ocr():
    try:
        # Capture the screen within the trade window region
        screenshot = pyautogui.screenshot(region=trade_window_region)

        # Convert the screenshot to a format that pytesseract can process
        trade_window_image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

        # Perform OCR on the captured image
        ocr_result = pytesseract.image_to_string(trade_window_image)

        # Process the OCR result (e.g., extract relevant information)
        process_ocr_result(ocr_result)
    except Exception as e:
        print(f"Error capturing and processing trade window: {str(e)}")


# Function to process the OCR result (customize this based on your needs)
def process_ocr_result(ocr_text):
    # Implement logic to extract and use information from the OCR result
    print("OCR Result:")
    print(ocr_text)


# Function to save annotated data to a file
def save_annotated_data():
    with open(annotated_data_file, 'w') as file:
        for item in annotated_data:
            file.write(f"{item}\n")


# Continuous screen capture and OCR
while True:
    capture_trade_window_and_ocr()

    # Allow the user to manually label and teach the OCR
    user_input = input("Type 'train' to teach the OCR, 'exit' to quit: ")

    if user_input == 'train':
        # Capture the region again
        screenshot = pyautogui.screenshot(region=trade_window_region)
        trade_window_image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

        # Convert the image to a NumPy array for OpenCV processing
        image_np = np.array(trade_window_image)

        # Display the captured image
        cv2.imshow("Captured Image", image_np)

        # Prompt the user to draw bounding boxes around text regions
        print("Draw bounding boxes around text regions and press 's' to save annotations...")
        while True:
            cv2.imshow("Captured Image", image_np)
            key = cv2.waitKey(1)

            if key == ord('s'):
                break

        # Extract text from the annotated image using OCR
        annotated_text = pytesseract.image_to_string(image_np)

        # Append annotated data to the list
        annotated_data.append(annotated_text)

        # Save annotated data to the file
        save_annotated_data()

        # Close the image display window
        cv2.destroyAllWindows()

    elif user_input == 'exit':
        break
