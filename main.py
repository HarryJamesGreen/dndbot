import tkinter as tk
from tkinter import ttk
import pytesseract
import logging
import csv
import time
import keyboard
import subprocess
from src.gui import OCRGui
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results
from tqdm import tqdm
import threading

# Path to the LibreOffice Calc executable
libreoffice_executable = r"C:\Program Files\LibreOffice\program\scalc.exe"
# Path to your spreadsheet file
spreadsheet_file = r"C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\docs\processed_data.csv"

# Configure logging
logging.basicConfig(filename='docs/ocr.log', level=logging.INFO)

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Variable to store the user's choice
perform_training = None


def clear_csv_file(filename):
    # Open the CSV file in write mode, which clears its contents
    with open(filename, 'w', newline='') as file:
        pass


def save_raw_ocr_to_csv(text, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])


def get_training_choice():
    global perform_training

    # Create a dialog window for user choice
    choice_window = tk.Tk()
    choice_window.title("Training Choice")

    def train_ocr_and_close():
        global perform_training
        perform_training = "yes"
        choice_window.destroy()

    def continue_without_training_and_close():
        global perform_training
        perform_training = "no"
        choice_window.destroy()

    # Create "Yes" and "No" buttons in the dialog window
    display_window = tk.Label(choice_window, text="Do you want to train OCR?"
                                                   "\nThis will take a few minutes.")
    display_window.pack()

    yes_button = ttk.Button(choice_window, text="Yes", command=train_ocr_and_close)
    no_button = ttk.Button(choice_window, text="No", command=continue_without_training_and_close)

    yes_button.pack()
    no_button.pack()

    choice_window.mainloop()


def train_ocr():
    for _ in range(3):  # Loop only three times
        perform_ocr_and_annotation()


def main():
    gui = None  # Initialize gui variable here

    # Initialize the Tkinter GUI in a separate thread
    def run_gui():
        nonlocal gui  # Use the outer gui variable
        root = tk.Tk()
        gui = OCRGui(root)
        gui.run()

    gui_thread = threading.Thread(target=run_gui)
    gui_thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    gui_thread.start()

    # Ask the user if they want to train OCR
    get_training_choice()

    if perform_training == 'yes':
        train_ocr()

    # Clear the content of the CSV file before opening it
    clear_csv_file('docs/processed_data.csv')

    # Open LibreOffice Calc with the CSV file
    subprocess.Popen([libreoffice_executable, spreadsheet_file])

    while True:
        if keyboard.is_pressed('Esc'):
            print("Exiting the program...")
            break

        screenshot, region = capture_dark_and_darker_window()
        if screenshot:
            screenshot.save("screenshot.png", "PNG")
            try:
                text = pytesseract.image_to_string('screenshot.png')
                logging.info(f"Extracted Text: {text}")
                save_raw_ocr_to_csv(text, 'docs/output.csv')

            except UnicodeDecodeError as e:
                logging.error(f"UnicodeDecodeError: {e}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")

            # Process OCR results with a progress bar
            for i in tqdm(range(100), desc="Processing OCR results", ascii=False, ncols=75):
                processed_data_list = process_ocr_results(text)
                time.sleep(0.01)  # Simulating a delay

                # Update the GUI table with the processed data
                if gui_thread.is_alive():
                    gui.update_table(processed_data_list)
                else:
                    logging.warning("The GUI thread has exited")
                    break



if __name__ == '__main__':
    main()
