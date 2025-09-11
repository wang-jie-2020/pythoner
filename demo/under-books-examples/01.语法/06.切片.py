if __name__ == '__main__':
    L = list(range(100))
    print(L[:])  # 全部

    print(L[:10])  # 前10个数
    print(L[10:20])  # 前11-20个数
    print(L[:10:2])  # 前10个数，每两个取一个
    print(L[::5])  # 每5个取一个

    print(L[-10:])  # 后10个数
