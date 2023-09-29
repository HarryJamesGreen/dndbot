def main():
    # Define the region to capture (you can adjust these values)
    region = (100, 100, 300, 300)

    # Capture the screen region
    screenshot = capture_screen(region)

    # Extract text from the screenshot
    text = extract_text_from_image(screenshot)
    print(f"Extracted Text: {text}")

    # Example: Move mouse to a position (you can adjust these values)
    move_mouse_to_position(150, 150)
