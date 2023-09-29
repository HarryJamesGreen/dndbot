from src.screen_capture import capture_screen
from src.text_extraction import extract_text_from_image
import time

def main():
    while True:
        # Capture the chat window
        screenshot = capture_specific_window(window_title='Dark and Darker')

        # Extract text from the screenshot
        chat_content = extract_text_from_image(screenshot)

        # Process new messages (avoid duplicates)
        new_messages = chat_content.difference(previous_chat_content)
        for message in new_messages:
            # Process each new message (e.g., save to CSV, display in console/GUI, etc.)
            process_message(message)

        # Update the previous chat content
        previous_chat_content = chat_content

        # Wait for a few seconds before capturing again
        time.sleep(5)  # Adjust the interval as needed


def process_message(message):
    # Your code to process/save/display each new message
    pass


if __name__ == '__main__':
    main()