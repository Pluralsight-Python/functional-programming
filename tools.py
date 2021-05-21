"""
    Example Usage of functional-style tools (functions): map, filter, reduce
"""
from functools import reduce
from math import factorial


def hexint(num):
    return int(num, base=16)


def combi(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def test_map():
    """Converting str MAC ID to IntArray of MAC ID Octets"""
    mac_str = "AB-CD-EF-01-02-03"
    m = map(hexint, mac_str.split('-'))

    print(m, m.__class__)
    print(list(m))

    """Calculate combinatorial"""
    nk = [(7, 4), (9, 1), (4, 2), (8, 3)]
    m = map(combi, [x[0] for x in nk], [x[1] for x in nk])

    print(m, m.__class__)
    print(list(m))


def test_filter():
    l = [True, 89, False, 1, 0, (3,), [], [2, 8], {}, {2}, {3: 9}]
    l2 = filter(None, l)

    print(l2, l2.__class__)
    print(list(l2))

    l3 = filter(lambda x: type(x) != list, l)
    print(l3, l3.__class__)
    print(list(l3))


def test_reduce():
    # Find sum
    l = [23, 78, 56, 98, 43, 90]

    res = reduce(lambda x, y: x + y, l)
    print(res)

    l = []
    res = reduce(lambda x, y: x + y, l, 0)
    print(res)


def map_filter_reduce():
    """ Sum of squares of odd numbers """
    # ans = reduce(lambda x, y: x + y, list(map(lambda x: x * x, list(filter(lambda y: y // 2, range(1, 100))))))

    odds = list(filter(lambda y: y % 2, range(1, 10)))
    squares = list(map(lambda x: x * x, odds))
    ans = reduce(lambda x, y: x + y, squares)

    print(odds)
    print(squares)
    print(ans)


if __name__ == '__main__':
    test_map()
    print()
    test_filter()
    print()
    test_reduce()
    print()
    map_filter_reduce()