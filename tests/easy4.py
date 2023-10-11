import tkinter as tk
import threading
import queue
import logging

logging.basicConfig(level=logging.DEBUG)

class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        self.geometry("300x200")
        self.label = tk.Label(self, text="Waiting for update...")
        self.label.pack(pady=20)

    def update_label(self, text):
        self.label.config(text=text)

def update_gui(app, data_queue):
    try:
        text = data_queue.get_nowait()
    except queue.Empty:
        logging.warning("Data queue is empty")
    else:
        app.update_label(text)
    app.after(100, update_gui, app, data_queue)

def worker_thread(data_queue):
    for i in range(10):
        data_queue.put(f"Update {i}")
        logging.info(f"Put Update {i} into the queue")

def main():
    app = SimpleGUI()
    data_queue = queue.Queue()

    # Start worker thread
    worker = threading.Thread(target=worker_thread, args=(data_queue,), daemon=True)
    worker.start()

    # Schedule the first GUI update
    app.after(100, update_gui, app, data_queue)

    # Start the Tkinter main loop
    app.mainloop()

    # Wait for the worker thread to finish
    worker.join()

if __name__ == "__main__":
    main()
