import tkinter as tk
import logging
import pytesseract
from src.data_processing import process_ocr_results
from src.screen_capture import capture_dark_and_darker_window
from src.Training import perform_ocr_and_annotation
from src.gui import OCRGui
import keyboard
import time
import tkinter.ttk as ttk

# Configure logging
logging.basicConfig(filename='ocr.log', level=logging.INFO)

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_training_choice():
    choice_window = tk.Tk()
    choice_window.title("Training Choice")
    user_choice = tk.BooleanVar(value=False)

    def on_yes():
        user_choice.set(True)
        choice_window.destroy()

    def on_no():
        user_choice.set(False)
        choice_window.destroy()

    tk.Label(choice_window, text="Do you want to train OCR?\nThis will take a few minutes.").pack()
    ttk.Button(choice_window, text="Yes", command=on_yes).pack()
    ttk.Button(choice_window, text="No", command=on_no).pack()

    choice_window.mainloop()
    return user_choice.get()


def train_ocr():
    for _ in range(3):
        perform_ocr_and_annotation()


def perform_ocr(image_path):
    try:
        text = pytesseract.image_to_string(image_path)
        logging.info(f"Extracted Text: {text}")
        return text
    except Exception as e:
        logging.error(f"An error occurred during OCR: {str(e)}")
        return None


def main():
    # Initialize GUI
    root = tk.Tk()
    gui = OCRGui(root)

    # Check if the user wants to train OCR
    perform_training = get_training_choice()
    if perform_training:
        train_ocr()

    while True:
        if keyboard.is_pressed('Esc'):
            print("Exiting the program...")
            break

        # 1. Capture Screenshot
        screenshot, _ = capture_dark_and_darker_window()
        if screenshot:
            screenshot_path = "screenshot.png"
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
        csv_file_path = 'output.csv'
        processed_data_list = process_ocr_results(extracted_text, screenshot_path, csv_file_path)

        # Update GUI
        if processed_data_list:
            gui.update_table(processed_data_list)

        # Optional: Add a delay before the next iteration
        time.sleep(1)

    # Start GUI main loop
    root.mainloop()


if __name__ == '__main__':
    main()
