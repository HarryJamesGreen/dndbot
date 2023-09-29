def move_mouse_to_position(x, y):
    """
    Moves the mouse to the specified x and y coordinates.

    Parameters:
    - x (int): X-coordinate.
    - y (int): Y-coordinate.
    """
    pyautogui.moveTo(x, y)