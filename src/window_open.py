import pygetwindow as gw
import time
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import matplotlib.pyplot as plt
from src.guiDND import DndBotGUI
from src.data_processing import process_ocr_results
from main import update_gui
import queue
import threading


from screenshot_dnd import screenshot_dnd_left_half

def show_message_box(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    response = messagebox.askretrycancel(title, message)

    return response

def wait_for_window(window_title):
    tk.Tk().withdraw()  # Hide the root window

    while True:
        dark_and_darker_window = gw.getWindowsWithTitle(window_title)

        if dark_and_darker_window:
            print(f"'{window_title}' window is open.")
            screenshot = Image.open("screenshot_dnd_left_half.png")
            plt.imshow(screenshot)
            plt.axis('on')  # Turn off axis labels
            plt.show()
            break
        else:
            print(f"Waiting for '{window_title}' window...")
            time.sleep(1)  # Wait for 1 second before checking again

            response = show_message_box("Window Not Found", f"'{window_title}' window not found. Retry or Continue?")
            if response == "Retry":
                continue
            elif response == "Continue":
                print("Continuing with the program...")
                break  # Exit the loop and continue with the program
            else:
                print("Exiting program.")
                exit(0)

if __name__ == "__main__":
    window_title = "DARK AND DARKER"  # Replace with the actual window title
    response = wait_for_window(window_title)

    if response == "Continue":
        # Continue with the program
        screenshot_file_path = "screenshot_dnd_left_half.png"
        csv_file_path = "processed_dnd_left_half.png"
        root = tk.Tk()  # Create a Tkinter root object
        app = DndBotGUI(master=root)  # Initialize your OCRGui object

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

