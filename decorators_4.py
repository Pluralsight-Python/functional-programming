"""
    Multiple Decorators
"""
import socket

from decorators_1 import get_exec_time
from decorators_2 import Tracer


class CallCount:
    def __init__(self):
        self.count = 0

    def __call__(self, f):
        def main(*args, **kwargs):
            self.count += 1
            print(f"Call Count of '{f.__name__}()': {self.count}")
            return f(*args, **kwargs)
        return main


call_counter = CallCount()


@Tracer
@call_counter
@get_exec_time
def resolve_host(host: str):
    return socket.gethostbyname(host)


if __name__ == '__main__':
    web_addresses = ['pluralsight.com', 'google.com', 'yahoo.com', 'duckduckgo.com', 'lenovo.com', 'dell.com']

    for addr in web_addresses:
        print(f"Resolved Address for '{addr}': {resolve_host(addr)}")

