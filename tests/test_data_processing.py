from tests.test_speedtest import measure_execution_time
from src.data_processing import process_ocr_results

# speedtest for function extract_text_from_image
# execution time: 0.0519 seconds

def test_data_processing():
    for i in range(5):
        # Sample OCR text for testing
        sample_ocr_text = '../docs/annotated_data.txt'

        # Measure execution time with sample OCR text
        execution_time = measure_execution_time(process_ocr_results, sample_ocr_text)

if __name__ == '__main__':
    main()