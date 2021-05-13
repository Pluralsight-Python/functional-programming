
from timeit import timeit
from callable_class_instance import Resolver


if __name__ == '__main__':
    resolver = Resolver()
    print("Test 1:")
    websites = ('google.com', 'pluralsight.com', 'duckduckgo.com')

    for w in websites:
        time_s = timeit(stmt='resolver(w)', number=1, globals=globals())
        print(f'{w}: {resolver(w)} | Resolved in {time_s * 1000:.3f}ms')

    print("\nResolve again:")

    for w in websites:
        time_s = timeit(stmt='resolver(w)', number=1, globals=globals())
        print(f'{w}: {resolver(w)} | Resolved in {time_s * 1000:.3f}ms')

