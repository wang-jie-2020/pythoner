def method1():

    classmates = ('Michael', 'Bob', 'Tracy')
    print('classmates =', classmates)
    print('len(classmates) =', len(classmates))
    print('classmates[0] =', classmates[0])
    print('classmates[1] =', classmates[1])
    print('classmates[2] =', classmates[2])
    print('classmates[-1] =', classmates[-1])

    try:
        classmates[0] = 'Adam'
        print('classmates =', classmates)
    except Exception as e:
        print(e)

def method2():
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)

if __name__ == '__main__':
    method1()
    print('----')
    method2()