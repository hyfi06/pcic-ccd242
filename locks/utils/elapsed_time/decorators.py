import functools
import time
import sys

from utils.elapsed_time.tools import print_elapsed_time, print_time


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print_time(start)
        try:
            result = func(*args, **kwargs)
        except KeyboardInterrupt:
            end = print_time()
            print_elapsed_time(start, end)
            sys.exit("KeyboardInterrupt")
        except Exception as e:
            end = print_time()
            print_elapsed_time(start, end)
            raise e
        end = print_time()
        print_elapsed_time(start, end)
        return result
    return wrapper
