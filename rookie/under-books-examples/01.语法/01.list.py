
"""
    切片运算是形如`[start:end:stride]`的运算符，其中`start`代表访问列表元素的起始位置，`end`代表访问列表元素的终止位置（终止位置的元素无法访问），而`stride`则代表了跨度，简单的说就是位置的增量
"""

def makeList():
    items1 = [35, 12, 99, 68, 55, 35, 87]
    items2 = ['Python', 'Java', 'Go', 'Kotlin']
    items3 = [100, 12.3, 'Python', True]
    print(items1)  # [35, 12, 99, 68, 55, 35, 87]
    print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
    print(items3)  # [100, 12.3, 'Python', True]

    items5 = [35, 12, 99, 45, 66]
    items6 = [45, 58, 29]
    items7 = ['Python', 'Java', 'JavaScript']
    print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
    items5 += items6
    print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
    print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

def sliceList():
    items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
    print(items8[0])  # apple
    print(items8[2])  # pitaya
    print(items8[4])  # watermelon
    items8[2] = 'durian'
    print(items8)  # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
    print(items8[-5])  # 'apple'
    print(items8[-4])  # 'waxberry'
    print(items8[-1])  # watermelon
    items8[-4] = 'strawberry'
    print(items8)  # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

    print(items8[1:3:1])  # ['strawberry', 'durian']
    print(items8[0:3:1])  # ['apple', 'strawberry', 'durian']
    print(items8[0:5:2])  # ['apple', 'durian', 'watermelon']
    print(items8[-4:-2:1])  # ['strawberry', 'durian']
    print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']

#def enumerableList():
def iterateList():
    languages = ['Python', 'Java', 'C++', 'Kotlin']
    for index in range(len(languages)):
        print(languages[index])

    for language in languages:
        print(language)

def operateList():
    classmates = ['Michael', 'Bob', 'Tracy']
    print('classmates =', classmates)

    classmates.append('Adam')
    print('classmates =', classmates)

    classmates.insert(1, 'Jack')
    print('classmates =', classmates)

    classmates.pop()
    print('classmates =', classmates)

    tmp = classmates.pop(1)
    print('classmates =', classmates)

    classmates.append('Bob')
    classmates.remove("Bob")
    print('classmates =', classmates)   # 只会移除第一个

def sliceList2():

    L = list(range(100))
    print(L[:])  # 全部
    print(L[:10])  # 前10个数
    print(L[10:20])  # 前11-20个数
    print(L[:10:2])  # 前10个数，每两个取一个
    print(L[::5])  # 每5个取一个
    print(L[-10:])  # 后10个数

if __name__ == '__main__':
    operateList()

