class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n

if __name__ == '__main__':
    foo("0")