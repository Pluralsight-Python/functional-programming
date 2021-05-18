#!/usr/bin/env python3
import datetime
import random
import time
from typing import List
from reprlib import repr


def get_exec_time(func):
    """
        Calculate exec time of any function
        NOTE: This function can be used as a decorator

    :param func: function name whose exec time is to be calculated
    :return: A wrapper function object enclosing call to supplied function
    """
    def wrapper(*args, **kwargs):
        start_us = datetime.datetime.now().timestamp() * 10**6
        ret = func(*args, **kwargs)
        end_us = datetime.datetime.now().timestamp() * 10**6
        exec_time_us = end_us - start_us
        print(f"'{func.__name__}()' took {exec_time_us:.3f}us to execute")
        return ret
    return wrapper


@get_exec_time
def calc_squares(nums: List):
    return [x * x for x in nums]


if __name__ == '__main__':
    l = [random.randint(1, 100) for _ in range(100000)]

    print(f"Orig List: {repr(l)}")
    sq = calc_squares(l)
    print(f"Squares: {repr(sq)}")

