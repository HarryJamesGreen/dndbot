import logging
import queue
import threading
import tkinter as tk
import tkinter.messagebox as messagebox  # Import the messagebox module
import pytesseract
from src.Training import perform_ocr_and_annotation
from PIL import Image, ImageTk
from src.guiDND import DndBotGUI
from src.data_processing import process_ocr_results

# Logging setup
logging.basicConfig(filename='dndbot.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def update_gui(app, data_queue):
    # Your existing update_gui function remains the same
    if not isinstance(data_queue, queue.Queue):
        logging.critical(f"data_queue is not a queue! It's a: {type(data_queue)}")
        return
    try:
        # Try to get data from the queue
        progress_value, csv_file_path, screenshot_file_path = data_queue.get_nowait()
    except queue.Empty:
        # Log a warning if the queue is empty
        logging.warning("Data queue is empty")
    except ValueError:
        # Log an error if data unpacking fails
        logging.error("Failed to unpack values from the data queue")
    else:
        # Update the GUI if data unpacking is successful
        app.update_progress_bar(progress_value)
        app.update_text_box_with_csv_data(csv_file_path)
        app.update_image(screenshot_file_path)
    # Schedule the next update
    app.after(100, update_gui, app, data_queue)  # Check the queue every 100ms

def start_training():
    # Add your training logic here
    logging.info("Training OCR")
    perform_ocr_and_annotation()

def main():
    # Ask the user if they want to do training
    choice = messagebox.askyesno("Training", "Do you want to perform OCR training?")
    if choice:
        start_training()
        return  # Exit the program after training

    # Create the Tkinter window and DndBotGUI object here
    screenshot_file_path = "screenshot_dnd_left_half.png"
    csv_file_path = "processed_dnd_left_half.png"
    root = tk.Tk()  # Create a Tkinter root object
    app = DndBotGUI(master=root)  # Initialize your DndBotGUI object

    data_queue = queue.Queue()

    # Start the OCR thread
    ocr_thread = threading.Thread(target=process_ocr_results,
                                  args=(data_queue, screenshot_file_path, csv_file_path),
                                  daemon=True)  # Set daemon=True to ensure the thread exits with the main program
    ocr_thread.start()

    # Schedule the first GUI update
    app.after(100, update_gui, app, data_queue)

    # Start the Tkinter main loop
    root.mainloop()

    # Wait for the OCR thread to finish
    ocr_thread.join()

if __name__ == "__main__":
    main()

