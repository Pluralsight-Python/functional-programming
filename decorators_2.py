"""
Using class objects as decorator
"""
import random


class Tracer:
    # Register/Remember the decorated function...
    def __init__(self, func):
        self._f = func

    def __call__(self, *args, **kwargs):
        print(f"Tracing '{self._f.__name__}{args}'")
        ret = self._f(*args, **kwargs)
        return ret


@Tracer
def rand_num(low, high):
    """
        Return random number between 'low' and 'high'
    """
    return random.randint(low, high)


@Tracer
def fibonacci():
    first = 1
    nexxt = 1
    yield first
    yield nexxt
    while True:
        first, nexxt = nexxt, nexxt + first
        yield nexxt


if __name__ == '__main__':
    g = fibonacci()

    for _ in range(5):
        x = rand_num(10, 99)
        print(f"Got {x}")
        print(f"Got {next(g)}")

    print("Metadata:")
    f = rand_num
    print(f"Name: {f.__str__()}")
    print(f"Type: {f.__class__}")
    print(f"Doc: {f.__doc__}")
