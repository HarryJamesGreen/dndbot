import time


def measure_execution_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.

    Parameters:
    - func (callable): The function to be measured.
    - *args, **kwargs: Arguments and keyword arguments to pass to the function.

    Returns:
    - float: Execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time