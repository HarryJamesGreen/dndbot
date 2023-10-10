import tkinter as tk
from src.gui import OCRGui


def test_gui():
    root = tk.Tk()
    gui = OCRGui(root)

    # Dummy data
    processed_data_list = [["Data1", "Data2"], ["Data3", "Data4"]]
    csv_file_path = 'processed_data.txt'
    screenshot_path = "test_screenshot.png"

    # Update GUI
    gui.update_table(processed_data_list)
    gui.update_text_box_with_csv_data(csv_file_path)
    gui.update_image(screenshot_path)

    root.mainloop()


test_gui()