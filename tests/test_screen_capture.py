from tests.test_speedtest import measure_execution_time
from src.screen_capture import capture_dark_and_darker_window


def test_screen_capture():
    execution_time = measure_execution_time(capture_dark_and_darker_window)
    print(f'Execution time for capture_dark_and_darker_window: {execution_time:.4f} seconds')


if __name__ == '__main__':
    main()