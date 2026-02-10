def add_end(L=[]):  # 强行解释?
    if L is None:
        L = []
    L.append('END')
    return L


def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

if __name__ == '__main__':
    print(add_end())
    print(add_end())
    print(add_end())

    print(add_end2())
    print(add_end2())
    print(add_end2())