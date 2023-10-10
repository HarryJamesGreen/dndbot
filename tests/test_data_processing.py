import unittest
from src.data_processing import process_ocr_results  # Ensure this import is correct
import os

class TestOCRProcessing(unittest.TestCase):
    def test_process_ocr_results(self):
        # Example usage
        text = "[7:26:38 AM] cheppy : [Gold Ore]x3 600g"
        expected_output = ['7:26:38 AM', 'cheppy', 'Gold Ore', 'x3', '600g']

        # Call the function
        ans = process_ocr_results(text)

        # Check the output
        self.assertEqual(ans, expected_output)


if __name__ == '__main__':
    unittest.main()
