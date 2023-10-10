import csv
import re
import logging

# Setup logging
logging.basicConfig(
    filename='process_ocr_results.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
