"""
    Class Instances as Decorators
"""
from typing import List


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def trace(*args, **kwargs):
            if self.enabled:
                print(f"Called {f}")
            ret = f(*args, **kwargs)
            print(ret)
            return ret
        return trace


tracer = Trace()


@tracer
def rotate_list(l: List):
    return l[1:] + l[0:1]


if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5]

    l = rotate_list(l)
    l = rotate_list(l)
    l = rotate_list(l)
    l = rotate_list(l)
    l = rotate_list(l)
    l = rotate_list(l)
