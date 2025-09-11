"""
    这里的例子不太好
"""

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

if __name__ == '__main__':
    f = count()
    print(f[0]())
    print(f[1]())
    print(f[2]())

    f = count2()
    print(f[0]())
    print(f[1]())
    print(f[2]())
