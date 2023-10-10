import threading
import queue
import time

def producer(data_queue):
    count = 0
    while count < 5:
        data_queue.put(f"Data {count}")
        count += 1
        time.sleep(1)

def consumer(data_queue):
    while True:
        data = data_queue.get()
        print("Received:", data)
        time.sleep(1)

data_queue = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(data_queue,), daemon=True)
consumer_thread = threading.Thread(target=consumer, args=(data_queue,), daemon=True)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()