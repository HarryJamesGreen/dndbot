import tkinter as tk
import tkinter.ttk as ttk
import logging
import pytesseract
from src.data_processing import process_ocr_results
from src.Training import perform_ocr_and_annotation, image_copy
from src.screenshot_dnd import screenshot_dnd_left_half
import keyboard
import csv
import logging
import traceback
import pytesseract
import os
from PIL import Image, ImageTk
from src.screenshot_dnd import screenshot_dnd_left_half
from src.data_processing import process_ocr_results
import tkinter as tk
import tkinter.ttk as ttk
import logging
import pytesseract
import csv
from PIL import Image, ImageTk
import logging
import time
import traceback
import threading
import queue
from src.gui import OCRGui  # Import the OCRGui class from gui.py
annotated_data_file = 'annotated_data.txt'
# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("process_log.log", mode='a', encoding='utf-8'),
                              logging.StreamHandler()])
screenshot_dnd_left_half()
print("Logging to process_log.log and console...")

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_training_choice(gui):
    print("break 1")
    choice_window = tk.Tk()
    choice_window.title("Training Choice")
    user_choice = tk.BooleanVar(value=False)
    tk.Label(choice_window, text="Do you want to train OCR?\nThis will take a few minutes.").pack()

    def on_yes():
        print("break 2 (YES)...")
        user_choice.set(True)
        choice_window.destroy()
        # If the user chooses to train, perform training
        if user_choice.get():
            progress_value = 0  # Set an initial progress value
            train_ocr(gui, progress_value)  # Pass the progress value to train_ocr

    def on_no():
        print("Break 3 (NO)...")
        user_choice.set(False)
        choice_window.destroy()

    ttk.Button(choice_window, text="Yes", command=on_yes).pack()
    ttk.Button(choice_window, text="No", command=on_no).pack()

    choice_window.mainloop()

    # Start the OCR loop and output to the GUI
    gui.clear_text_box()  # Clear the text box
    ocr_loop(gui)  # Start the OCR loop and output to the GUI
    return user_choice.get()


def train_ocr(gui, progress_value):
    try:
        print("performing ocr training")

        # Call the function from Training.py
        perform_ocr_and_annotation()

        # Update the progress bar with the specified progress value
        gui.update_progress_bar(progress_value)

        # After training, update the GUI with the image
        gui.update_image_with_bounding_box(image_copy)  # Pass the image_copy with bounding box drawing

        # You can add more training logic here if needed
    except Exception as e:
        logging.error(f"An error occurred during OCR training: {str(e)}")

def perform_ocr(image_path):
    try:
        text = pytesseract.image_to_string(image_path)
        logging.info(f"Extracted Text: {text}")
        print(f"Extracted Text: {text}")  # Add this line for testing
        return text
    except Exception as e:
        logging.error(f"An error occurred during OCR: {str(e)}")
        logging.error("Traceback: ")
        logging.error(traceback.format_exc())  # Log the full traceback
        return None


def test_ocr_export():
    try:
        with open(annotated_data_file, 'r') as file:
            annotated_data = file.read().splitlines()

        if annotated_data:
            print("Annotated Data:")
            for item in annotated_data:
                print(item)
        else:
            print("No annotated data found.")
    except Exception as e:
        print(f"An error occurred while testing OCR export: {str(e)}")

# Call the test function to check OCR export
test_ocr_export()

def ocr_loop(data_queue):
    try:
        ocr_count = 0  # Initialize OCR count

        while True:
            if keyboard.is_pressed('Esc'):
                print("Exiting the program...")
                break

            # 1. Capture Screenshot
            screenshot, _ = screenshot_dnd_left_half()
            if screenshot:
                screenshot_path = "screenshot_dnd_left_half.png"
                screenshot.save(screenshot_path, "PNG")
            else:
                logging.error("Screenshot capture failed.")
                continue

            # 2. Perform OCR
            extracted_text = perform_ocr(screenshot_path)
            if not extracted_text:
                logging.error("OCR failed or extracted empty text.")
                continue

            # 3. Process OCR Results
            csv_file_path = 'processed_data.csv'
            processed_data_list = process_ocr_results(extracted_text, screenshot_path, csv_file_path)

            # Update OCR count and progress bar
            ocr_count += 1

            # Log every tenth OCR process
            if ocr_count % 10 == 0:
                logging.info(f"Performed {ocr_count} OCR processes.")

            # Put data into the queue
            data_queue.put((processed_data_list, csv_file_path, screenshot_path))

    except Exception as e:
        logging.error(f"An error occurred in the OCR loop: {str(e)}")


def update_gui(gui, data_queue):
    try:
        # Check if there is data in the queue
        processed_data_list, csv_file_path, screenshot_path = data_queue.get_nowait()
        # Update GUI
        if processed_data_list:
            gui.update_table(processed_data_list)
            gui.update_text_box_with_csv_data(csv_file_path)
            gui.update_image(screenshot_path)
    except queue.Empty:
        pass  # Handle an empty queue
    except Exception as e:
        logging.error(f"An error occurred while updating the GUI: {str(e)}")


def main():
    try:
        # Initialize GUI
        root = tk.Tk()
        gui = OCRGui(root)

        # Check if the user wants to train OCR
        perform_training = get_training_choice(gui)  # Pass the GUI instance to get_training_choice

        if perform_training:
            for progress_value in range(0, 101, 10):  # Example: Update progress in increments of 10
                # Start the training process and update the progress bar accordingly
                train_ocr(gui, progress_value)
                time.sleep(1)  # Add a delay between training iterations

        data_queue = queue.Queue()  # Create a queue

        # Start the OCR loop in a separate thread
        ocr_thread = threading.Thread(target=ocr_loop, args=(data_queue,), daemon=True)
        ocr_thread.start()

        # Start periodic GUI update
        gui.root.after(100, update_gui, gui, data_queue)

        # Start GUI main loop
        root.mainloop()

    except Exception as e:
        logging.error("An unexpected error occurred.")
        logging.error(str(e))
        logging.error("Traceback: ")
        logging.error(traceback.format_exc())  # Log the full traceback


if __name__ == '__main__':
    main()
