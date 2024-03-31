from datetime import datetime
import time
import math

# Part 1
def clock(n):
    # Your code here
    """
    Prints clock that runs for n seconds.
    """
    end_time = time.time() + n
    while time.time() < end_time:
        print("\r" + datetime.now().strftime("%H:%M:%S"), end="", flush=True)
        time.sleep(1)
        if time.time() == end_time:
            break

# Part 2
def lcm(a, b):
    # Your code here
    """
    Returns lowest common multiple of integers a and b

    Example
    >>>>>
    lcm(2, 3)
    6
    """
    a_original = a
    b_original = b
    if a == b:
        return a 
    while True: 
        if a < b:
            a += a_original
        else:
            b += b_original
        if a == b:
            return a

# Part 3
def gcf(a, b):
    # Your code here
    """
    Returns greates comman factor of a and b
    """
    while b != 0:
        r = a % b
        a = b
        b = r

    return a