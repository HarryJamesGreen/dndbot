import unittest
from PIL import Image
from src.screen_capture import capture_screen


class TestScreenCapture(unittest.TestCase):

    def test_screen_capture(self):
        # Define a small region for testing
        region = (0, 0, 100, 100)
        screenshot = capture_screen(region)
        self.assertIsInstance(screenshot, Image.Image, "The captured screen is not an instance of PIL Image.")

