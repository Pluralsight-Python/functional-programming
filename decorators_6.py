"""
    Passing parameters to decorators, like in functools.wrap
"""
import functools


# This function emulates functools.wrap

# This function is NOT the actual decorator
# While decorating, this function is called and it returns 'f' which is the actual decorator
def wrap(wrapped_func):
    print(f"Wrapped func: {wrapped_func.__name__}")     # This will be printed at runtime without even calling main()

    def f(wrapping_func):
        print(f"Wrapping func: {wrapping_func.__name__}")

        def wrapper(*args, **kwargs):
            wrapper.__doc__ = wrapped_func.__doc__
            wrapper.__name__ = wrapped_func.__name__
            return wrapping_func(*args, **kwargs)
        return wrapper
    return f


def test_decorator(func):
    print(f"Decorator for {func.__name__}")             # This too...

    @wrap(func)
    def test_wrapper(*args, **kwargs):
        print("Test Wrapper")
        return func(*args, **kwargs)
    return test_wrapper


@test_decorator
def test_func(s):
    """Test Function"""
    print(f"Hello {s}")
    print(f"Metadata => Name: {test_func.__name__}, Doc: {test_func.__doc__}")


def test_decorator_2(func):
    print(f"Decorator for {func.__name__}")

    @functools.wraps(func)
    def test_wrapper(*args, **kwargs):
        print("Test Wrapper")
        return func(*args, **kwargs)
    return test_wrapper


@test_decorator_2
def test_func_2(s):
    """Test Function"""
    print(f"Hello {s}")
    print(f"Metadata => Name: {test_func.__name__}, Doc: {test_func.__doc__}")


if __name__ == '__main__':
    print()
    test_func("World!!")
    print()
    test_func_2("Sonam!!")

