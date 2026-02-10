import functools
import time

def log(func):
    def wrapper(*args, **kw):
        print('wrapper call %s():' % func.__name__)
        print('wrapper args:', args)
        print('wrapper kw:', kw)
        return func(*args, **kw)

    return wrapper


@log
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


@log
def person2(name, age, *, city, job):
    print(name, age, city, job)


@log
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

if __name__ == '__main__':
    person('Michael', 30)
    person('Adam', 45, gender='M', job='Engineer')
    person2('Jack', 24, city='Beijing', job='Engineer')
    person3('Bob', 35, '', 1, True, city='Beijing', job='Engineer')

