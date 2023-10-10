import logging
import queue
import threading
import tkinter as tk
import pytesseract
from PIL import Image, ImageTk
import src.data_processing as dp
import src.guiDND as gui
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Logging setup
logging.basicConfig(filename='dndbot.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def get_training_choice(gui):
    # Removed duplicate print statements
    print("Training OCR")
    gui.update_text_box("Training OCR")


def train_ocr(gui):
    # Removed unused parameter 'progress_value'
    print("Training OCR")
    gui.update_text_box("Training OCR")


def perform_ocr(image_path):
    # This function is not used in the original main.py
    # If it's needed, it should be called/used in the appropriate logic flow
    print("Performing OCR")
    ocr_text = pytesseract.image_to_string(Image.open(image_path))
    return ocr_text


def test_ocr_export():
    # This function is called in the original main.py but does not seem to have a practical application
    # If it's needed, it should be called/used in the appropriate logic flow
    print("Testing OCR Export")


def update_gui(gui, data_queue):
    try:
        # Added exception handling for unpacking values from the queue
        progress_value, csv_file_path, screenshot_file_path = data_queue.get_nowait()
    except queue.Empty:
        # Handle empty queue case
        logging.warning("Data queue is empty")
    except ValueError:
        # Handle value unpacking issues
        logging.error("Failed to unpack values from the data queue")
    else:
        # Update GUI only if data unpacking is successful
        gui.update_progress_bar(progress_value)
        gui.update_text_box_with_csv_data(csv_file_path)
        gui.update_image(screenshot_file_path)


def main():
    screenshot_file_path = "screenshot_dnd_left_half.png"
    csv_file_path = "processed_dnd_left_half.png"

    root = tk.Tk()
    app = gui.OCRGui(master=root)

    data_queue = queue.Queue()

    ocr_thread = threading.Thread(target=dp.process_ocr_results,
                                  args=(data_queue, screenshot_file_path, csv_file_path))
    ocr_thread.start()

    gui_update_thread = threading.Thread(target=update_gui,
                                         args=(app, data_queue))
    gui_update_thread.start()

    root.mainloop()  # Ensure you're calling mainloop on the Tkinter root object

    ocr_thread.join()
    gui_update_thread.join()


if __name__ == "__main__":
    main()
