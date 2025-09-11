def method1():
    classmates = ['Michael', 'Bob', 'Tracy']
    print('classmates =', classmates)
    print('len(classmates) =', len(classmates))
    print('classmates[0] =', classmates[0])
    print('classmates[1] =', classmates[1])
    print('classmates[2] =', classmates[2])
    print('classmates[-1] =', classmates[-1])

    classmates.append('Adam')
    print('classmates =', classmates)

    classmates.insert(1, 'Jack')
    print('classmates =', classmates)

    classmates.pop()
    print('classmates =', classmates)

    classmates.pop(1)
    print('classmates =', classmates)

if __name__ == '__main__':
    method1()

