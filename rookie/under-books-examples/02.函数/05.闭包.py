def createCounter():
    num = 0

    def counter():
        return num + 1

    return counter


def createCounter2():
    num = 0

    def counter():
        nonlocal num    # 访问外层, 需要nonlocal
        num = num + 1
        return num

    return counter


if __name__ == '__main__':
    f = createCounter()
    print(f())  # 1
    print(f())  # 1

    f2 = createCounter2()
    print(f2()) # 1
    print(f2()) # 2
