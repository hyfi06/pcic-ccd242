import functools
import time
import sys

from elapsed_time.tools import print_time, print_elapsed_time


def execution_time(print_function=print_elapsed_time):
    def upper_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            print_time(start)
            try:
                result = func(*args, **kwargs)
            except KeyboardInterrupt:
                end = print_time()
                print_function(start, end)
                sys.exit("KeyboardInterrupt")
            except Exception as e:
                end = print_time()
                print_function(start, end)
                raise e
            end = print_time()
            print_function(start, end)
            return result
        return wrapper
    return upper_wrapper
