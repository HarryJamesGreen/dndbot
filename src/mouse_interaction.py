import pyautogui
import random
import time


def jiggle_mouse(x, y, radius=5, duration=5):
    """
    Jiggle the mouse around the specified (x, y) coordinate.

    Parameters:
    - x, y: The central coordinates around which the mouse will jiggle.
    - radius: The radius of the area around the central point in which the mouse will move.
    - duration: The duration in seconds for which the mouse will keep jiggling.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        # Calculate a random offset from the central point
        dx = random.randint(-radius, radius)
        dy = random.randint(-radius, radius)

        # Move the mouse to the new position
        pyautogui.moveTo(x + dx, y + dy, duration=0.1)

        # Wait for a short duration before the next movement
        time.sleep(0.2)
