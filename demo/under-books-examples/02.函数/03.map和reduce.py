from functools import reduce

def f(x):
    return x * x


def fn(x, y):
    return x * 10 + y


def is_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print(reduce(fn, [1, 3, 4, 5]))

    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
