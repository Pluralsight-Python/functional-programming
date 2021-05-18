"""
    Preserving function metadata with functools.wrap
"""
import functools

from typing import Callable


def print_metadata(func):
    print(f"Name: {func.__name__}")
    print(f"Doc: {func.__doc__}")


def no_wrap(func: Callable):
    def wrapper(*args, **kwargs):
        print("Actual Function Metadata: ")
        print_metadata(func)
        return func(*args, **kwargs)
    return wrapper


def with_wrap(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Actual Function Metadata: ")
        print_metadata(func)
        return func(*args, **kwargs)
    return wrapper


def undecorated():
    """This is undecorated function
    """
    print(f"Undecorated function called...")


@with_wrap
def decorated_with_wrap():
    """This is decorated function with decorator using functools.wrap
    """
    print(f"Decorated_with_wrap function called...")


@no_wrap
def decorated_no_wrap():
    """This is decorated function with decorator NOT using functools.wrap
    """
    print(f"Decorated_no_wrap function called...")


if __name__ == '__main__':
    print("1. Calling 'undecorated'")
    undecorated()
    print("Metadata:")
    print_metadata(undecorated)
    print("\n\n2. Calling 'decorated_no_wrap'")
    decorated_no_wrap()
    print("Metadata:")
    print_metadata(decorated_no_wrap)
    print("\n\n3. Calling 'decorated_with_wrap'")
    decorated_with_wrap()
    print("Metadata:")
    print_metadata(decorated_with_wrap)

