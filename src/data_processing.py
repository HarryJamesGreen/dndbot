# data_processing.py

def remove_duplicates_from_list(data_list):
    """
    Removes duplicates from a given list while preserving the order.

    Parameters:
    - data_list (list): The list from which duplicates need to be removed.

    Returns:
    - list: A list with duplicates removed.
    """
    seen = set()
    unique_list = []
    for item in data_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list
