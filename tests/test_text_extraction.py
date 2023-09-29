from tests.test_speedtest import measure_execution_time
from src.csv_exporter import export_to_csv


def test_text_extraction():
    # Sample data and filename for testing
    sample_data = [
        {'timestamp': '2023-09-29 12:00:00', 'name': 'John', 'item': 'Sword', 'price': '100'},
        {'timestamp': '2023-09-29 12:05:00', 'name': 'Jane', 'item': 'Shield', 'price': '150'}
    ]
    sample_filename = 'docs/processed_data.csv'

    # Measure execution time with sample arguments
    execution_time = measure_execution_time(export_to_csv, sample_data, sample_filename)

if __name__ == '__main__':
    main()