"""
1. Create decorator for the following function that will
- add line to the opened file containing the number of times function was called
- line format "Starting function call: "

2. Create decorator for the following function that will
- force all args and kwargs to the type specified as decorator arg
"""
from functools import wraps


def add_line(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        f = open('file', "w")
        f.write('Starting function call: ' + str(wrapper.calls))
        f.close()
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def set_type(obj_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return obj_type(func(*args, **kwargs))
        return wrapper
    return decorator


@set_type(str)
@add_line
def open_file(name, mode='r'):
    return open(name, mode)


open_file('file.txt', "w")
open_file('file.txt', "w")
open_file('file.txt', "w")
open_file(1, 'w')

