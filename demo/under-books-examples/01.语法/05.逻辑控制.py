import sys

def method1():
    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')

def method2():

    score = 'B'
    match score:
        case 'A':
            print('score is A.')
        case 'B':
            print('score is B.')
        case 'C':
            print('score is C.')
        case _:  # _表示匹配到其他任何情况
            print('score is ???.')

def method3():
    age = 15

    match age:
        case x if x < 10:
            print(f'< 10 years old: {x}')
        case 10:
            print('10 years old.')
        case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
            print('11~18 years old.')
        case 19:
            print('19 years old.')
        case _:
            print('not sure.')

def method4(args):
    match args:
        # 如果仅出现gcc，报错:
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 出现gcc，且至少指定了一个文件:
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')

def method5():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)

    for x in range(10):
        print(x)

def method6():
    sum = 0
    n = 1
    while n <= 100:
        sum = sum + n
        n = n + 1
    print(sum)

if __name__ == '__main__':
    method1()
    method2()
    method3()
    method4(args = ['gcc', 'hello.c', 'world.c'])
    method4(args = ['gcc'])
    method5()
    method6()
